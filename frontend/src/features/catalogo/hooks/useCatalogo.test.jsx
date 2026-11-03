import { describe, it, expect, vi, beforeEach } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useCatalogo } from './useCatalogo';
import * as api from '../api';

vi.mock('../api');

describe('useCatalogo Hook', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  // Carga inicial: loading=true -> loading=false con datos
  it('debe iniciar en loading=true y pasar a loading=false con los datos cargados', async () => {
    const mockData = {
      items: [
        { id: 1, titulo: 'Curso de prueba 1' },
        { id: 2, titulo: 'Curso de prueba 2' }
      ],
      total: 2
    };

    api.fetchCursos.mockResolvedValueOnce(mockData);

    const { result } = renderHook(() => useCatalogo());

    expect(result.current.loading).toBe(true);

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(result.current.cursos).toEqual(mockData.items);
    expect(result.current.total).toBe(2);
    expect(result.current.error).toBeNull();
  });

  // Error de red: estado de error seteado, lista vacía
  it('debe manejar errores de red seteando el estado de error y vaciando la lista', async () => {
    api.fetchCursos.mockRejectedValueOnce(new Error('Error al obtener el catálogo de cursos'));

    const { result } = renderHook(() => useCatalogo());

    await waitFor(() => {
      expect(result.current.loading).toBe(false);
    });

    expect(result.current.error).toBe('Error al obtener el catálogo de cursos');
    expect(result.current.cursos).toEqual([]);
    expect(result.current.total).toBe(0);
  });

  // setPage(n) -> recarga con page=n (y resetea a 1 si cambia el filtro)
  it('debe actualizar la pagina y resetear a 1 cuando cambia un filtro', async () => {
    api.fetchCursos.mockResolvedValue({ items: [], total: 0 });

    const { result } = renderHook(() => useCatalogo());

    await waitFor(() => expect(result.current.loading).toBe(false));

    act(() => {
      result.current.setPage(3);
    });

    await waitFor(() => expect(result.current.loading).toBe(false));

    expect(result.current.page).toBe(3);
    expect(api.fetchCursos).toHaveBeenLastCalledWith({
      page: 3,
      q: '',
      categoriaId: null
    });

    act(() => {
      result.current.setFiltro({ q: 'Testing' });
    });
    await waitFor(() => expect(result.current.loading).toBe(false));

    expect(result.current.page).toBe(1);
    expect(result.current.q).toBe('Testing');
    expect(api.fetchCursos).toHaveBeenLastCalledWith({
      page: 1,
      q: 'Testing',
      categoriaId: null
    });
  });

  // refetch() -> recarga con parámetros actuales
  it('debe volver a pedir los datos con parametros actuales al llamar a refetch()', async () => {
    api.fetchCursos.mockResolvedValue({ items: [{ id: 1, titulo: 'Curso Base' }], total: 1 });

    const { result } = renderHook(() => useCatalogo({ page: 2, q: 'Prueba' }));

    await waitFor(() => expect(result.current.loading).toBe(false));

    expect(api.fetchCursos).toHaveBeenCalledTimes(1);

    await act(async () => {
      await result.current.refetch();
    });
    await waitFor(() => expect(result.current.loading).toBe(false));

    expect(api.fetchCursos).toHaveBeenCalledTimes(2);
    expect(api.fetchCursos).toHaveBeenLastCalledWith({
      page: 2,
      q: 'Prueba',
      categoriaId: null
    });
  });
});