# Image Prompting Guide (Nano Banana)

## 🎨 Core Principles
The `generate_image` tool uses the Gemini 2.5 Flash Image model. To get the best results, structure your prompts effectively.

### 1. Style & Medium
Always specify *how* it should look.
-   **Photorealistic**: "A 8k highly detailed photograph of..."
-   **Artistic**: "Watercolor painting of...", "Oil painting in the style of Van Gogh...", "Charcoal sketch..."
-   **Digital**: "3D render, blender style...", "Pixel art...", "Flat vector illustration..."
-   **Vibe**: "Cyberpunk", "Steampunk", "Minimalist", "Vintage 1950s".

### 2. Lighting & Atmosphere
-   "Golden hour lighting", "Cinematic lighting", "Neon lights", "Soft diffused light", "Dark and moody".

### 3. Composition
-   "Wide angle shot", "Close up macro", "Bird's eye view", "Symmetrical composition".

## 🛠️ Specialized Tools

### Icons (`generate_icon`)
Best for App Icons or UI.
-   **Parameters**:
    -   `style`: `flat`, `skeuomorphic`, `minimal`, `modern`.
    -   `background`: `transparent`, `white`, or hex color.
    -   `corners`: `rounded` or `sharp`.
-   *Example*: "A minimalist rocket ship icon, blue gradient, flat style."

### Patterns (`generate_pattern`)
Best for wallpapers or textures.
-   **Parameters**:
    -   `type`: `seamless` (tiles perfectly).
    -   `density`: `sparse`, `medium`, `dense`.
-   *Example*: "Geometric triangles, pastel colors, seamless pattern."

### Diagrams (`generate_diagram`)
Best for explaining concepts.
-   **Types**: `flowchart`, `mindmap`, `architecture`, `network`.
-   *Example*: "A flowchart showing the process of photosynthesis."

## 🔄 Editing & Consistency (`generate_story`)
-   **Story**: Generates 2-8 sequential images. Great for storyboards.
    -   *Tip*: Keep the prompt focused on the *sequence* of events.
-   **Edit**: Use `edit_image` to change parts of an existing image.
    -   *Prompt*: "Change the red car to a blue truck."
