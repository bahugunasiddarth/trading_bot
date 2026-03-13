import argparse

def validate_positive(value):
    """Validates that a numeric input is positive."""
    float_val = float(value)
    if float_val <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid positive float value")
    return float_val

def validate_inputs(args):
    """Business logic validation for order parameters."""
    errors = []
    
    if args.side.upper() not in ['BUY', 'SELL']:
        errors.append(f"Invalid side: {args.side}. Must be BUY or SELL.")
        
    if args.type.upper() not in ['MARKET', 'LIMIT']:
        errors.append(f"Invalid type: {args.type}. Must be MARKET or LIMIT.")
        
    if args.type.upper() == 'LIMIT' and args.price is None:
        errors.append("Price is required for LIMIT orders.")
        
    if errors:
        raise ValueError(" | ".join(errors))
        
    return True