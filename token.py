import argparse
import sys
from pathlib import Path

# Try to import tiktoken
try:
    import tiktoken
    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False

DIST_DIR = Path("dist")

def get_token_count(text: str, model_name: str) -> tuple[int, str]:
    """
    Calculates token count and returns the method used.
    Returns: (count, method_type)
    method_type values: 'exact', 'fallback', 'approx'
    """
    if TIKTOKEN_AVAILABLE:
        try:
            encoding = tiktoken.encoding_for_model(model_name)
            return len(encoding.encode(text)), "exact"
        except KeyError:
            # Model name not found in tiktoken -> Fallback to cl100k_base
            encoding = tiktoken.get_encoding("cl100k_base")
            return len(encoding.encode(text)), "fallback"
    else:
        # Library missing -> Character approximation
        return len(text) // 3, "approx"

def print_header(model_name: str):
    """Prints the table header."""
    print(f"Target Model: {model_name}")
    print(f"{'File Name':<40} | {'Tokens':>10} | {'Chars':>10} | {'Note':<15}")
    print("-" * 83)

def analyze_file(file_path: Path, model_name: str):
    """Reads a file and prints statistics with a note on the calculation method."""
    try:
        content = file_path.read_text(encoding="utf-8")
        token_count, method = get_token_count(content, model_name)
        char_count = len(content)
        
        # Determine display note based on method
        note = ""
        token_str = f"{token_count:,}"
        
        if method == "fallback":
            note = "⚠️ Est. (OpenAI)" # Estimated using OpenAI base
            token_str += "*"
        elif method == "approx":
            note = "⚠️ Est. (Char)"   # Estimated using chars
            token_str += "*"
            
        print(f"{file_path.name:<40} | {token_str:>10} | {char_count:>10,} | {note:<15}")
        return token_count
    except Exception as e:
        print(f"Error reading {file_path.name}: {e}")
        return 0

def analyze_all(model_name: str):
    """Scans and analyzes all files."""
    files = sorted(list(DIST_DIR.glob("*.md")))
    
    if not files:
        print(f"No Markdown files found in {DIST_DIR}.")
        return

    print_header(model_name)
    
    total_tokens = 0
    for file_path in files:
        total_tokens += analyze_file(file_path, model_name)
    
    print("-" * 83)
    print(f"Total Files: {len(files)}")
    
    # Print footer explanation if needed
    print("\n[Legend]")
    print("  (Empty) : Exact calculation using tiktoken for the specified model.")
    print("  * : Estimated value.")
    print("  Fallback: Model not found in tiktoken. Used 'cl100k_base' (GPT-4 standard) as reference.")

def main():
    """
    Entry point: Parses command line arguments and runs the analysis.
    """
    # Check if dist directory exists
    if not DIST_DIR.exists():
        print(f"Error: Dist directory not found: {DIST_DIR}")
        print("Please run build.py first to generate the prompt files.")
        sys.exit(1)

    # Setup Argument Parser
    parser = argparse.ArgumentParser(description="Calculate tokens for generated prompts.")
    
    # Positional argument for filename (optional)
    parser.add_argument(
        "file_name", 
        nargs="?", 
        help="The specific filename in 'dist' to analyze. If omitted, analyzes all files."
    )

    # Optional argument for model name
    parser.add_argument(
        "-m", "--model",
        default="gpt-4o",
        help="The target model name for token calculation (e.g., gpt-4, gpt-3.5-turbo). Default: gpt-4o"
    )
    
    args = parser.parse_args()

    # Warn if tiktoken is missing
    if not TIKTOKEN_AVAILABLE:
        print("Warning: 'tiktoken' library not found. Using rough approximation.")
        print("Install with 'pip install tiktoken' for accurate results.\n")

    # Dispatch logic
    if args.file_name:
        # Analyze specific file
        file_name = args.file_name
        if not file_name.endswith(".md"):
            file_name += ".md"
            
        target_path = DIST_DIR / file_name
        
        if not target_path.exists():
            print(f"Error: File not found: {target_path}")
            sys.exit(1)
            
        print_header(args.model)
        analyze_file(target_path, args.model)
    else:
        # Analyze all files
        analyze_all(args.model)

if __name__ == "__main__":
    main()