#!/bin/bash
# StateBase Python SDK Release Script

set -e

# 1. Verification
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$BRANCH" != "main" ]; then
  echo "❌ Error: Releases must be made from the 'main' branch."
  exit 1
fi

if [[ -n $(git status -s) ]]; then
  echo "❌ Error: Working directory is dirty. Please commit or stash changes."
  exit 1
fi

# 2. Versioning
CURRENT_VERSION=$(python setup.py --version)
echo "Current version: $CURRENT_VERSION"
echo "Enter new version (e.g., 0.5.0):"
read NEW_VERSION

if [ -z "$NEW_VERSION" ]; then
  echo "❌ Error: Version cannot be empty."
  exit 1
fi

# Update setup.py (simple sed replace)
# Note: This assumes version="x.y.z" format exactly as it is now
sed -i "s/version=\"$CURRENT_VERSION\"/version=\"$NEW_VERSION\"/" setup.py

# 3. Build
echo "📦 Building package..."
rm -rf build/ dist/ *.egg-info
python -m build

# 4. Git Operations
echo "🐙 Committing version bump..."
git add setup.py
git commit -m "chore: bump version to $NEW_VERSION"
git tag -a "v$NEW_VERSION" -m "Release v$NEW_VERSION"

# 5. Publish
echo "🚀 Next steps:"
echo "1. git push origin main --tags"
echo "2. twine upload dist/*"
echo ""
echo "Do you want to push to Git now? (y/n)"
read PUSH_GIT
if [ "$PUSH_GIT" == "y" ]; then
  git push origin main --tags
fi

echo "Do you want to upload to PyPI now? (y/n)"
read PUSH_PYPI
if [ "$PUSH_PYPI" == "y" ]; then
  twine upload dist/*
fi

echo "✅ Done!"
