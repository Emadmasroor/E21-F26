#!/bin/bash
# Made by Google Gemini

# 1. Set the message (Custom or Default)
COMMIT_MSG=${1:-"website re-render"}

echo "🚀 Starting re-render..."

# 2. Run Quarto Render
quarto render

# 3. Save the newly rendered index.html to a temp file
# 'mktemp' creates a unique path like /tmp/tmp.aB123CD
TEMP_FILE=$(mktemp)
cp docs/Labs/index.html "$TEMP_FILE"
echo "💾 Temporary backup of index.html created."

# 4. Restore folders from Git
echo "📂 Restoring Labs and Markdeep folders to HEAD..."
git checkout HEAD -- docs/Labs
git checkout HEAD -- docs/markdeep

# 5. Move the saved index.html back into the folder
cp "$TEMP_FILE" docs/Labs/index.html
rm "$TEMP_FILE"
echo "♻️ Rendered index.html restored to docs/Labs/"

# 6. Git Add, Commit, and Push
echo "⬆️ Pushing changes..."
git add .
git commit -m "$COMMIT_MSG"
git push

echo "🎉 Done!"
