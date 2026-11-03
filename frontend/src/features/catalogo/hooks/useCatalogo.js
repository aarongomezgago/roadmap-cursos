import { useState, useEffect, useCallback } from 'react';
import { fetchCursos } from '../api';

export function useCatalogo(initialParams = {}) {
  const [cursos, setCursos] = useState([]);
  const [total, setTotal] = useState(0);
  const [page, setPageState] = useState(initialParams.page || 1);
  const [q, setQState] = useState(initialParams.q || '');
  const [categoriaId, setCategoriaIdState] = useState(initialParams.categoriaId || null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const loadCursos = useCallback(async (p, query, catId) => {
    setLoading(true);
    setError(null);
    try {
      const data = await fetchCursos({ page: p, q: query, categoriaId: catId });
      setCursos(data.items || []);
      setTotal(data.total || 0);
    } catch (err) {
      setError(err.message || 'Error de red');
      setCursos([]);
      setTotal(0);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadCursos(page, q, categoriaId);
  }, [page, q, categoriaId, loadCursos]);

  const setPage = (newPage) => {
    setPageState(newPage);
  };

  const setFiltro = ({ q: newQ, categoriaId: newCatId }) => {
    if (newQ !== undefined) setQState(newQ);
    if (newCatId !== undefined) setCategoriaIdState(newCatId);
    setPageState(1);
  };

  const refetch = () => {
    return loadCursos(page, q, categoriaId);
  };

  return {
    cursos,
    total,
    page,
    q,
    categoriaId,
    loading,
    error,
    setPage,
    setFiltro,
    refetch,
  };
}
