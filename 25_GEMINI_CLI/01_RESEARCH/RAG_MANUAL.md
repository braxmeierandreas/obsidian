# RAG & File Search Manual

## 📂 What is File Search (RAG)?
Retrieval Augmented Generation (RAG) allows me to "read" and "remember" large documents that don't fit in my immediate context window. I can search through them to answer specific questions with citations.

## 🛠️ The Workflow

### 1. Upload & Index
Before I can read a file, it must be uploaded to a "Store".
-   **Tool**: `file_search_upload`
-   **Input**: A local file path (PDF, DOCX, TXT, MD, CSV) or a folder.
-   **Result**: The file is processed, chunked, and stored in the cloud (Google File Search API).
-   *Note*: Stores persist for 48 hours or until deleted (depending on policy).

### 2. Querying
Once uploaded, I don't need to read the whole file again. I just search it.
-   **Tool**: `file_search_query`
-   **Input**: Your question + The Store Name.
-   **Process**:
    1.  I convert your question into a vector.
    2.  I find the most relevant "chunks" of text in your documents.
    3.  I generate an answer based *only* on those chunks.

### 3. Management
-   **List Stores**: `file_search_list_stores` (See what's available).
-   **Delete Store**: `file_search_delete_store` (Clean up).
-   **Create Store**: `file_search_create_store` (Organize by topic, e.g., "Thesis Sources").

## 🚀 Deep Research Integration
I can combine **Deep Research** with **File Search**.
-   **Command**: `research_start`
-   **Parameter**: `fileSearchStoreNames`
-   **Effect**: I will research the internet *AND* your uploaded documents simultaneously to generate a comprehensive report.

## 💡 Best Practices
-   **Topic-Based Stores**: Create separate stores for different projects (e.g., "Uni_Biology", "Business_Plan").
-   **File Types**: PDFs and clean Text/Markdown files work best.
-   **Naming**: Give stores clear display names so we recognize them later.
