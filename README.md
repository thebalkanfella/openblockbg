# OpenBlockBG

[![English](https://img.shields.io/badge/lang-English-blue.svg)](README.md)
[![Български](https://img.shields.io/badge/lang-Български-red.svg)](README.bg.md)

**Open-source spam and scam phone number blocklist for Bulgaria and beyond.**

This project maintains a community-driven list of spam and scam phone numbers that can be imported into smartphones for blocking unwanted calls.

## 📥 Download

**[⬇️ Download blocked_contacts.vcf](blocked_contacts.vcf)**

Import this file to your phone to block all spam numbers in the list.

## Quick start

### Import to iPhone
1. Download [`blocked_contacts.vcf`](blocked_contacts.vcf)
2. Open the file on your iPhone
3. Tap "Add Contact"
4. Go to Settings → Phone → Blocked Contacts
5. Add the "OpenBlockBG" contact to blocked list

### Import to Android
1. Download [`blocked_contacts.vcf`](blocked_contacts.vcf)
2. Open Contacts app
3. Menu → Import
4. Select the VCF file
5. Go to Phone → Settings → Blocked Numbers
6. Add the "OpenBlockBG" contact to blocked list


## Features

- 📱 VCF (vCard) file format for easy import
- 🇧🇬 Focused on Bulgarian market with international support
- 📞 Compatible with iPhone and Android
- 🔄 Regular community-driven updates
- 🔓 Fully open-source and transparent

## Files

- [`spam_numbers.txt`](spam_numbers.txt) - Plain text list of spam phone numbers
- [`blocked_contacts.vcf`](blocked_contacts.vcf) - VCF file ready for import
- [`generate_vcf.py`](generate_vcf.py) - Script to generate VCF from the number list

## Format

Supported number formats:
- Bulgarian Mobile: 088888888, 087123456, 089123456
- Bulgarian Landline: 02XXXXXXX (Sofia), 032XXXXXX (Plovdiv)
- International: +1234567890, +44123456789, +359XXXXXXXX
- With formatting: +1 (555) 123-4567 (spaces and symbols will be cleaned)

## Contributing

Feel free to submit pull requests with new spam numbers. Please include:
- The spam phone number
- Brief description of the spam type (if known)
- Date when you received the spam call

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Legal Notice

This list is for educational and protection purposes only. Use responsibly and verify numbers before blocking to avoid blocking legitimate contacts.