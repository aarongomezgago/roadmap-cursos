# Builder
FROM python:3.12-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends binutils && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_PREFERENCE=only-system

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev --no-install-project

RUN uv cache clean && \
    find /app/.venv -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true && \
    find /app/.venv -type d -name "tests" -exec rm -rf {} + 2>/dev/null || true && \
    find /app/.venv -type d -name "test" -exec rm -rf {} + 2>/dev/null || true && \
    find /app/.venv -type f -name "*.pyc" -delete 2>/dev/null || true && \
    find /app/.venv -name "*.so" -exec strip --strip-unneeded {} + 2>/dev/null || true


# Runtime
FROM python:3.12-slim AS runtime

RUN rm -rf /usr/local/lib/python3.12/test \
           /usr/local/lib/python3.12/idlelib \
           /usr/local/lib/python3.12/ensurepip \
           /usr/local/lib/python3.12/tcl* \
           /usr/local/lib/python3.12/tkinter \
           /usr/local/lib/python3.12/turtle.py \
           /usr/local/lib/python3.12/unittest \
           /usr/local/lib/python3.12/pydoc_data \
           /usr/local/share/doc \
           /usr/local/share/man

RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY --chown=appuser:appuser app /app/app

ENV PATH="/app/.venv/bin:$PATH"

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]