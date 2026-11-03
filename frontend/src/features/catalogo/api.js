export async function fetchCursos({ page = 1, size = 20, q = '', categoriaId = null } = {}) {
  const params = new URLSearchParams({
    page: page.toString(),
    page_size: size.toString(),
  });

  if (q) params.append('q', q);
  if (categoriaId) params.append('categoria_id', categoriaId.toString());

  const response = await fetch(`/api/v1/cursos?${params.toString()}`);

  if (!response.ok) {
    throw new Error('Error de red al obtener el catálogo de cursos');
  }

  return await response.json();
}


export async function getCursos(params) {
 return fetchCursos(params);
}

