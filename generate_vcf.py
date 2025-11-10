#!/usr/bin/env python3
"""
OpenBlockBG - VCF Generator for Spam Numbers

This script reads spam phone numbers from spam_numbers.txt and generates
a VCF (vCard) file that can be imported into smartphones for blocking.
Supports both Bulgarian and international phone numbers.
"""

import re
from datetime import datetime

def read_spam_numbers(filename='spam_numbers.txt'):
    """Read spam numbers from text file, ignoring comments and empty lines."""
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                # Remove comments and whitespace
                line = line.split('#')[0].strip()
                if not line:
                    continue
                
                # Validate phone number format
                if is_valid_phone_number(line):
                    numbers.append(line)
                else:
                    print(f"Warning: Invalid number format on line {line_num}: {line}")
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []
    
    return numbers

def is_valid_phone_number(number):
    """Check if number is in valid format (Bulgarian or international)."""
    # Remove any spaces, dashes, parentheses, and other formatting
    clean_number = re.sub(r'[^\d+]', '', number)
    
    # Must have at least 7 digits and at most 15 (E.164 standard)
    if len(clean_number) < 7 or len(clean_number) > 15:
        return False
    
    # Bulgarian patterns (for backwards compatibility)
    bulgarian_patterns = [
        r'^08[789]\d{6}$',  # Mobile numbers
        r'^0[2-9]\d{7,8}$', # Landline numbers
        r'^\+359[2-9]\d{7,8}$',  # International format for Bulgaria
    ]
    
    # International patterns
    international_patterns = [
        r'^\+\d{7,14}$',  # International format: + followed by 7-14 digits
        r'^\d{7,15}$',    # Local format: 7-15 digits (will be treated as local)
    ]
    
    # Check all patterns
    all_patterns = bulgarian_patterns + international_patterns
    return any(re.match(pattern, clean_number) for pattern in all_patterns)

def format_number_for_vcf(number):
    """Format number for VCF file."""
    # Remove any spaces, dashes, parentheses and special characters except +
    clean_number = re.sub(r'[^\d+]', '', number)
    
    # If it already has international format (+...), keep it
    if clean_number.startswith('+'):
        return clean_number
    
    # If it's a Bulgarian local number, add +359 prefix
    if clean_number.startswith('0') and len(clean_number) >= 8:
        # Check if it looks like Bulgarian number
        if (clean_number.startswith('08') or 
            clean_number.startswith('02') or 
            clean_number.startswith('03') or 
            clean_number.startswith('04') or 
            clean_number.startswith('05') or 
            clean_number.startswith('06') or 
            clean_number.startswith('07') or 
            clean_number.startswith('09')):
            return '+359' + clean_number[1:]
    
    # For other numbers without international prefix, assume they need one
    # But don't add +359 since we don't know the country
    if not clean_number.startswith('+'):
        # Return as-is and let user specify the correct international format
        return '+' + clean_number
    
    return clean_number

def generate_vcf(numbers, output_filename='blocked_contacts.vcf'):
    """Generate VCF file with a single contact containing all phone numbers."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if not numbers:
        print("No numbers to generate VCF file")
        return
    
    with open(output_filename, 'w', encoding='utf-8') as vcf_file:
        # Create single vCard entry with multiple phone numbers
        vcf_file.write('BEGIN:VCARD\n')
        vcf_file.write('VERSION:3.0\n')
        vcf_file.write('FN:OpenBlockBG\n')
        vcf_file.write('N:OpenBlockBG;;;;\n')
        vcf_file.write('ORG:OpenBlockBG - Community Blocklist\n')
        
        # Add all phone numbers to the same contact
        for i, number in enumerate(numbers):
            formatted_number = format_number_for_vcf(number)
            # Use different TYPE labels for multiple numbers
            tel_type = f'VOICE,HOME' if i == 0 else f'VOICE,WORK' if i == 1 else f'VOICE,OTHER'
            vcf_file.write(f'TEL;TYPE={tel_type}:{formatted_number}\n')
        
        vcf_file.write(f'NOTE:OpenBlockBG spam blocklist - Updated {timestamp}. Contains {len(numbers)} verified spam numbers.\n')
        vcf_file.write('END:VCARD\n')
    
    print(f"Generated {output_filename} with 1 contact containing {len(numbers)} spam numbers")

def main():
    """Main function to generate VCF file from spam numbers."""
    print("OpenBlockBG - Spam Numbers VCF Generator")
    print("=========================================")
    
    # Read spam numbers
    numbers = read_spam_numbers()
    if not numbers:
        print("No valid spam numbers found!")
        return
    
    print(f"Found {len(numbers)} valid spam numbers:")
    for number in numbers:
        print(f"  - {number}")
    
    # Generate VCF file
    generate_vcf(numbers)
    print("\nDone! Import blocked_contacts.vcf to your phone to block these numbers.")
    print("\nInstructions:")
    print("iPhone: Open VCF → Add Contact → Settings → Phone → Blocked Contacts → Add contact")
    print("Android: Contacts → Import → Phone → Settings → Blocked Numbers → Add contact")

if __name__ == '__main__':
    main()