#!/usr/bin/env python3
"""
VCF Generator for Bulgarian Spam Numbers

This script reads spam phone numbers from spam_numbers.txt and generates
a VCF (vCard) file that can be imported into smartphones for blocking.
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
                if is_valid_bulgarian_number(line):
                    numbers.append(line)
                else:
                    print(f"Warning: Invalid number format on line {line_num}: {line}")
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []
    
    return numbers

def is_valid_bulgarian_number(number):
    """Check if number is in valid Bulgarian format."""
    # Remove any spaces or special characters
    clean_number = re.sub(r'[^\d+]', '', number)
    
    # Bulgarian mobile: 087/088/089 + 6 digits
    # Bulgarian landline: 02 + 7 digits (Sofia), others vary
    # International: +359...
    
    patterns = [
        r'^08[789]\d{6}$',  # Mobile numbers
        r'^0[2-9]\d{7,8}$', # Landline numbers
        r'^\+359[2-9]\d{7,8}$',  # International format
    ]
    
    return any(re.match(pattern, clean_number) for pattern in patterns)

def format_number_for_vcf(number):
    """Format number for VCF file."""
    # Remove any spaces or special characters except +
    clean_number = re.sub(r'[^\d+]', '', number)
    
    # If it's a local number, add +359 prefix
    if clean_number.startswith('0'):
        clean_number = '+359' + clean_number[1:]
    elif not clean_number.startswith('+'):
        # Assume it's already without leading 0
        clean_number = '+359' + clean_number
    
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
        vcf_file.write('FN:Bulgarian Spam Numbers\n')
        vcf_file.write('N:Spam;Bulgarian;Numbers;;\n')
        vcf_file.write('ORG:Blocked Contacts\n')
        
        # Add all phone numbers to the same contact
        for i, number in enumerate(numbers):
            formatted_number = format_number_for_vcf(number)
            # Use different TYPE labels for multiple numbers
            tel_type = f'VOICE,HOME' if i == 0 else f'VOICE,WORK' if i == 1 else f'VOICE,OTHER'
            vcf_file.write(f'TEL;TYPE={tel_type}:{formatted_number}\n')
        
        vcf_file.write(f'NOTE:Bulgarian spam numbers collection - blocked on {timestamp}. Contains {len(numbers)} spam numbers.\n')
        vcf_file.write('END:VCARD\n')
    
    print(f"Generated {output_filename} with 1 contact containing {len(numbers)} spam numbers")

def main():
    """Main function to generate VCF file from spam numbers."""
    print("Bulgarian Spam Numbers VCF Generator")
    print("====================================")
    
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