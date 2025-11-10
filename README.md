# Bulgarian Spam/Scam Phone Numbers

This project maintains a list of Bulgarian spam and scam phone numbers that can be imported into smartphones for blocking unwanted calls.

## Features

- 📱 VCF (vCard) file format for easy import
- 🇧🇬 Focused on Bulgarian spam numbers
- 📞 Compatible with iPhone and Android
- 🔄 Regular updates with new spam numbers

## Files

- `spam_numbers.txt` - Plain text list of spam phone numbers
- `blocked_contacts.vcf` - VCF file ready for import
- `generate_vcf.py` - Script to generate VCF from the number list

## Usage

### Import to iPhone
1. Download `blocked_contacts.vcf`
2. Open the file on your iPhone
3. Tap "Add All Contacts"
4. Go to Phone → Blocked Contacts
5. Add the imported contacts to blocked list

### Import to Android
1. Download `blocked_contacts.vcf`
2. Open Contacts app
3. Menu → Import
4. Select the VCF file
5. Go to Phone → Settings → Blocked Numbers
6. Add the imported contacts

### Adding New Numbers
1. Add the number to `spam_numbers.txt`
2. Run `python generate_vcf.py` to regenerate the VCF file
3. Commit and push changes

## Format

Numbers should be in Bulgarian format:
- Mobile: 088888888 (example spam number)
- Landline: 02XXXXXXX
- International: +359XXXXXXXX

## Contributing

Feel free to submit pull requests with new spam numbers. Please include:
- The spam phone number
- Brief description of the spam type (if known)
- Date when you received the spam call

## Legal Notice

This list is for educational and protection purposes only. Use responsibly and verify numbers before blocking to avoid blocking legitimate contacts.