# Gemini CLI Cheatsheet

## ⚡ System Commands
-   `/help`: Show available commands and tools.
-   `/bug`: Report an issue or provide feedback.
-   `/clear`: Clear the current conversation context (start fresh).
-   `/exit` or `/quit`: Close the CLI.

## 🛠️ Key Tool Commands
*Note: You usually just ask in natural language, but these are the direct functions.*

### File System
-   `list_directory`: See files in a folder.
-   `read_file`: Read content of a file.
-   `write_file`: Create or overwrite a file.
-   `search_file_content`: Find text inside files (Grep/Ripgrep).
-   `glob`: Find files by name pattern (e.g., `*.py`).

### Google Workspace
-   `gmail.search query="is:unread"`: Find emails.
-   `calendar.listEvents`: Check schedule.
-   `docs.create title="My Doc"`: New Google Doc.

### Research
-   `research_start input="..."`: Begin Deep Research.
-   `file_search_upload path="..."`: Upload file for RAG.
-   `file_search_query query="..."`: Ask questions to your files.

### Image
-   `generate_image prompt="..."`: Make an image.
-   `generate_icon prompt="..."`: Make an icon.

## ⌨️ Shortcuts & Tips
-   **Interrupt**: `Ctrl + C` (stops generation).
-   **Multiline Input**: Depending on your terminal, often `` at the end of a line or pasting text works.
-   **Context**: I know your current directory (`C:\Users\braxm\obsidian`). You can refer to files relatively (`./25_GEMINI_CLI/...`).
-   **Memory**: Tell me "Remember that..." to save facts to `save_memory`.

## 🤖 Sub-Agents
-   **Codebase Investigator**: Ask "Analyze this project structure" to activate.
-   **Ralph (Loop)**: `/ralph-loop "Fix this bug..."` (Iterative self-correction).
