FROM python:3.11-slim

#Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1


#work directory
WORKDIR /app

# installing system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

#copy all contents from local to app
COPY . .

# RUN setup.py
RUN pip install --no-chache-dir -e .

#USED PORTS
EXPOSE 8501

#RUN app
CMD ["streamlit", "run", "app.py", "--server.port=8501","server-address=0.0.0.0", "--server.headless=true"]


