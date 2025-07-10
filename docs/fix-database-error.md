The error you're seeing:

```
psycopg2.OperationalError: connection to server at "localhost" (127.0.0.1), port 5432 failed: FATAL:  database "fastapi_course_test" does not exist
```

means that your PostgreSQL is up and reachable, but the **database you're trying to connect to does not exist**.

---

### ✅ To fix this, you need to **create the database**:

Run the following command in your terminal:

```bash
createdb -U nouman -h localhost -p 5432 fastapi_course_test
```

It will prompt you for the password, enter:

```
noumanrehman042
```

If `createdb` is not available, you can use `psql`:

```bash
psql -U nouman -h localhost -p 5432 -c "CREATE DATABASE fastapi_course_test;"
```

---

### 🧪 To verify it was created:

You can list the databases:

```bash
psql -U nouman -h localhost -p 5432 -l
```

Make sure `fastapi_course_test` shows up in the list.

---

### 🔒 Security Tip (for production)

Never commit or expose raw credentials like:

```
user=nouman password=noumanrehman042
```

Instead, use environment variables and load them securely using `python-dotenv`, `os.environ`, or a secrets manager.

Let me know if you want help automating test DB creation or setting up a `.env` file.
