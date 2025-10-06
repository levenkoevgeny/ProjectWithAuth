FROM python:3.12-slim AS builder

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim

RUN useradd -m -r appuser && \
   mkdir /app && \
   chown -R appuser:appuser /app

RUN apt update
RUN apt install nano -y
RUN apt install mc -y

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /app

COPY --chown=appuser:appuser . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER appuser

COPY --chmod=777 --chown=appuser:appuser ./entrypoint.sh /app/
RUN chown -R appuser:appuser /app
RUN mkdir /app/static && chown -R appuser:appuser /app/static
ENTRYPOINT ["/app/entrypoint.sh"]