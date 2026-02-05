# Gemini CLI Skill Ecosystem

## 🔄 Dynamic Skill Activation
I don't just "know" things; I can "activate" specialized personas using the `activate_skill` tool. This changes my operating instructions to follow expert methodologies.

### How it Works
1.  **Trigger**: You ask for a task requiring expertise (e.g., "Review this paper").
2.  **Activation**: I call `activate_skill(name="peer-review")`.
3.  **Context**: I receive a specialized system prompt (XML wrapped) with strict rules and workflows.

### 📚 Available Skill Categories

#### 1. Co-Researcher (PhD Level)
*Best for academic and rigorous professional work.*
-   **Methodology**: `research-methodology`, `quantitative-analysis`, `qualitative-research`.
-   **Review**: `peer-review`, `ethics-review`, `critical-analysis`.
-   **Synthesis**: `research-synthesis`, `literature-review`, `systematic-review`.
-   **Management**: `research-manager`, `grant-proposal`.

#### 2. Advanced Search (Exa)
*Best for finding things Google misses.*
-   `web-search-advanced-research-paper`: Academic papers.
-   `web-search-advanced-financial-report`: SEC filings, earnings.
-   `company-research`: Business intel.
-   `get-code-context-exa`: Programming examples.

#### 3. Meta Skills
-   `skill-creator`: I can help you write *new* skills for me.

## 🛠️ Creating Your Own Skills
You can extend my capabilities by creating new skills. A skill is essentially a markdown file with strict instructions.

### The `skill-creator` Workflow
1.  **Idea**: Tell me "I want to create a skill for [Task, e.g., 'analyzing stock charts']".
2.  **Drafting**: I will activate `skill-creator` to guide you through defining:
    -   **Name**: Unique identifier.
    -   **Description**: When I should use it.
    -   **Instructions**: Step-by-step rules I must follow.
3.  **Deployment**: I save the file to the correct directory, and it becomes immediately available.

### Example Use Case
*User*: "Help me check if this news article is fake."
*Me*: Activates `multi-source-investigation`.
*Me (Skill Mode)*: "I will now cross-reference claims against primary sources..."
