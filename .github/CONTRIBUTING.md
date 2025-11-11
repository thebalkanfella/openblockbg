# Contributing to OpenBlockBG

Thank you for helping protect people from spam calls! OpenBlockBG is a community-driven project. 

## How to Add New Spam Numbers

1. **Fork the repository**
2. **Add the spam number** to `spam_numbers.md` in the correct format:
   ```
   088123456  # Description of spam type - Date received
   ```

3. **Number formats accepted:**
   - Bulgarian Mobile: `087123456`, `088123456`, `089123456`
   - Bulgarian Landline: `02XXXXXXX` (Sofia), `032XXXXXX` (Plovdiv), etc.
   - International: `+1234567890`, `+44123456789`, `+359XXXXXXXX`

5. **Commit the file:**
   ```bash
   git add spam_numbers.md
   git commit -m "Add spam number: 088123456"
   ```

6. **Create a pull request**

## Guidelines

- **Verify the number** is actually spam before adding
- **Add a comment** describing the spam type if possible
- **Use proper format** - the script validates phone numbers (Bulgarian and international)
- **Don't add personal numbers** or numbers you're unsure about
- **One number per line** in the text file

## Common Spam Types in Bulgaria

- Fake lottery/prize scams
- Bank/credit card scams  
- Insurance sales calls
- Fake technical support
- Survey scams
- Robocalls

## Questions?

Open an issue if you need help or have questions about contributing.