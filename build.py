import yaml
import argparse
import sys
from pathlib import Path

# Constants for directory paths
RECIPE_DIR = Path("recipes")
DIST_DIR = Path("dist")
ROOT_DIR = Path(".")

def build_recipe(recipe_path: Path):
    """
    Reads a YAML recipe configuration and generates a combined Markdown prompt file.
    Enforces the output filename to match the recipe filename (Convention over Configuration).
    """
    print(f"Building recipe: {recipe_path.name}...")

    # 1. Load YAML configuration
    try:
        with open(recipe_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading YAML: {e}")
        return

    output_filename = recipe_path.stem + ".md"
    
    modules = config.get("modules", [])
    full_content = []

    # 2. Assemble modules
    for module_path_str in modules:
        module_path = ROOT_DIR / module_path_str
        
        if not module_path.exists():
            print(f"  Warning: Module not found: {module_path}")
            continue
            
        # Read and strip whitespace to ensure clean joining
        text = module_path.read_text(encoding="utf-8").strip()
        
        # Skip empty files
        if text:
            full_content.append(text)

    # 3. Save the artifact
    DIST_DIR.mkdir(exist_ok=True)
    output_path = DIST_DIR / output_filename
    
    # [Optimization]
    # Join with double newline. 
    # This is sufficient for Markdown to recognize headers and separate paragraphs
    # without wasting tokens on visual separators like "---".
    final_text = "\n\n".join(full_content)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_text)
        
    print(f"Generated: {output_path}")

def build_all():
    """
    Scans the recipe directory and builds all found recipes.
    """
    recipes = list(RECIPE_DIR.glob("*.yaml"))
    
    if not recipes:
        print("No recipes found.")
        return

    for recipe in recipes:
        build_recipe(recipe)

def main():
    """
    Entry point: Parses command line arguments and dispatches build tasks.
    """
    # Check if recipe directory exists
    if not RECIPE_DIR.exists():
        print(f"Recipes directory not found: {RECIPE_DIR}")
        sys.exit(1)

    # Setup Argument Parser
    parser = argparse.ArgumentParser(description="Build system prompts from recipes.")
    parser.add_argument(
        "recipe_name", 
        nargs="?", 
        help="The name of the recipe file to build (e.g., 'backend_master'). If omitted, builds all recipes."
    )
    
    args = parser.parse_args()

    # Dispatch logic
    if args.recipe_name:
        # Build specific recipe
        recipe_name = args.recipe_name
        if not recipe_name.endswith(".yaml"):
            recipe_name += ".yaml"
            
        target_path = RECIPE_DIR / recipe_name
        
        if not target_path.exists():
            print(f"Error: Recipe file not found: {target_path}")
            sys.exit(1)
            
        build_recipe(target_path)
    else:
        # Build all recipes
        print("No recipe specified. Building all recipes...")
        build_all()
    
    print("\nBuild process completed.")

if __name__ == "__main__":
    main()