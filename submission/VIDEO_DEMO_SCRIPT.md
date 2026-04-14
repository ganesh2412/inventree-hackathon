# 5-Minute Video Demo Script
## InvenTree Parts Module - Hackathon 2026 Submission

**Author:** Ganesh H N  
**Duration:** 5 minutes  
**Format:** Google Slides Presentation + Quick Demo

---

## 🎬 Recording Setup

### Before You Start:
1. Close all unnecessary apps and notifications
2. Open only these tabs:
   - Google Slides presentation
   - GitHub repository (github.com/ganesh2412/inventree-hackathon)
   - InvenTree (http://localhost/web)
3. Set browser to fullscreen (Cmd+Shift+F)
4. Test your microphone
5. Have this script ready to read

### Recording Tools (Choose One):
- **Loom** (5-min limit): loom.com
- **QuickTime** (Mac built-in): File → New Screen Recording
- **OBS Studio** (Unlimited): obsproject.com

---

## 📝 Complete Narration Script

### SLIDE 1: Title Slide (15 seconds) ⏱️ 0:00-0:15

**ON SCREEN:** Title slide with "InvenTree Automation Testing - Hackathon 2026"

**SAY:**
> "Hello! I'm Ganesh H N, and this is my submission for the InvenTree Hackathon 2026. I've developed a comprehensive automated testing framework for the InvenTree Parts Module. Let me walk you through what I've built."

**TIMING TIP:** Speak slowly and clearly

---

### SLIDE 2: Project Overview (40 seconds) ⏱️ 0:15-0:55

**ON SCREEN:** Project Overview slide showing objectives, technologies, coverage, and repository

**SAY:**
> "My objective was to create complete automated testing for the InvenTree Parts Module. I used industry-standard technologies - Python with Pytest for API testing, Playwright for UI automation, and the Requests library for HTTP operations.
> 
> The framework provides comprehensive coverage with complete CRUD operations - that's Create, Read, Update, and Delete - testing both through the API and the user interface.
> 
> The entire codebase is available on my GitHub repository at github.com/ganesh2412/inventree-hackathon."

**TIMING TIP:** Emphasize "complete CRUD operations" and "API and UI"

---

### SLIDE 3: API Test Coverage (45 seconds) ⏱️ 0:55-1:40

**ON SCREEN:** API Test Coverage slide showing all operations

**SAY:**
> "For API automation, I've implemented tests covering all major operations.
> 
> For GET operations - we can list all parts with pagination support and retrieve individual parts by ID.
> 
> For POST operations - we create new parts with complete validation testing, including tests for missing fields and invalid data.
> 
> PATCH operations handle updating part details and data integrity verification.
> 
> And DELETE operations ensure parts are properly removed from the system.
> 
> Every single test includes authentication handling, response validation, status code verification, and data integrity checks."

**TIMING TIP:** Pause briefly between each operation type

---

### SLIDE 4: Framework Architecture (45 seconds) ⏱️ 1:40-2:25

**ON SCREEN:** Framework Architecture slide with repository structure

**SAY:**
> "The framework follows a clean, modular architecture. The repository is organized into two main sections:
> 
> The API folder contains all pytest-based tests using the Requests library, with fixtures for authentication and configuration.
> 
> The UI folder contains Playwright-based browser automation tests with reusable page objects and helper functions.
> 
> Key features include environment-based configuration using .env files, reusable test fixtures that eliminate code duplication, and a structure that makes it incredibly easy to extend with new test cases.
> 
> Everything follows pytest and Playwright best practices."

**TIMING TIP:** Emphasize "modular architecture" and "easy to extend"

---

### SLIDE 5: Live Demo - Switch to Browser (90 seconds) ⏱️ 2:25-3:55

**ON SCREEN:** Switch from slides to web browser

**ACTION:** Press Escape to exit slides, switch to browser tab with GitHub

**SAY:**
> "Now let me show you the actual implementation. Here's my GitHub repository."

**ACTION:** Navigate to https://github.com/ganesh2412/inventree-hackathon

**SAY:**
> "The README provides a complete overview with setup instructions and test coverage summary."

**ACTION:** Scroll down briefly to show README structure

**SAY:**
> "Let me show you the automation framework structure."

**ACTION:** Click on 'submission' → 'automation'

**SAY:**
> "Here you can see the API and UI folders. Each contains test files, configuration, and documentation."

**ACTION:** Click into 'api' → 'tests'

**SAY:**
> "These are the API test files - conftest for fixtures, and individual test files for each operation type."

**ACTION:** Go back and click 'ui' → 'tests'

**SAY:**
> "And here are the UI automation tests using Playwright."

**OPTIONAL:** If time permits, briefly show InvenTree running:

**ACTION:** Switch to InvenTree tab (http://localhost/web)

**SAY:**
> "The framework has been tested against this InvenTree instance, and all tests are passing successfully."

**TIMING TIP:** Keep the navigation smooth and purposeful

---

### SLIDE 6: Key Achievements - Back to Slides (30 seconds) ⏱️ 3:55-4:25

**ON SCREEN:** Switch back to Google Slides, Key Achievements slide

**ACTION:** Return to slides presentation

**SAY:**
> "To summarize the key achievements:
> 
> We have comprehensive test coverage for the Parts module, both API and UI automation frameworks working together, clean and maintainable code structure, easy extensibility for new test cases, proper configuration management, all tests passing successfully, and we're using industry-standard tools - Pytest and Playwright.
> 
> This framework is production-ready and can be integrated into any CI/CD pipeline."

**TIMING TIP:** Speak with confidence about achievements

---

### SLIDE 7: Thank You (35 seconds) ⏱️ 4:25-5:00

**ON SCREEN:** Thank You slide with repository and contact info

**SAY:**
> "Thank you for reviewing my submission!
> 
> The complete project including all source code, documentation, test cases, and setup instructions is available at github.com/ganesh2412/inventree-hackathon.
> 
> I'm Ganesh H N, and this has been my InvenTree Hackathon 2026 submission demonstrating comprehensive automated testing for the Parts Module.
> 
> If you have any questions or would like to see more details, please feel free to reach out. Thank you!"

**TIMING TIP:** End with a smile and confidence

---

## 📊 Timing Breakdown Summary

| Section | Duration | Total Time |
|---------|----------|------------|
| Slide 1: Title | 15s | 0:15 |
| Slide 2: Overview | 40s | 0:55 |
| Slide 3: API Coverage | 45s | 1:40 |
| Slide 4: Architecture | 45s | 2:25 |
| Slide 5: Live Demo | 90s | 3:55 |
| Slide 6: Achievements | 30s | 4:25 |
| Slide 7: Thank You | 35s | 5:00 |
| **TOTAL** | **5:00** | |

---

## ✅ Pre-Recording Checklist

- [ ] Close all unnecessary applications
- [ ] Disable notifications (Do Not Disturb mode)
- [ ] Open required tabs: Slides, GitHub, InvenTree
- [ ] Test microphone and audio quality
- [ ] Practice once without recording (time yourself)
- [ ] Print this script or have it on second screen
- [ ] Clear browser history bar if needed
- [ ] Set browser zoom to 100%
- [ ] Close bookmark bar for clean screen
- [ ] Have water nearby (for smooth speaking)

---

## 🎯 Tips for Best Results

### Voice Tips:
- Speak slightly slower than normal conversation
- Pause for 1-2 seconds between slides
- Emphasize key technical terms
- Use an enthusiastic but professional tone
- Smile while speaking (it shows in your voice!)

### Technical Tips:
- Record in a quiet room
- Use headphones with microphone if available
- Position microphone 6-12 inches from mouth
- Do a 10-second test recording first
- If you make a mistake, pause 3 seconds and restart that sentence

### Navigation Tips:
- Use keyboard shortcuts (spacebar for next slide)
- Keep mouse movements smooth and purposeful
- Don't rush through the GitHub navigation
- Let each page load fully before speaking

---

## 🔧 If Recording with Loom (5-min limit):

1. Install Loom desktop app
2. Click "Start Recording"
3. Select "Screen Only" or "Screen + Camera"
4. Choose which screen/window
5. Click the red button to start
6. Follow this script
7. Click stop when done
8. Loom automatically uploads
9. Get share link and add to README

---

## 🔧 If Recording with QuickTime (Unlimited):

1. Open QuickTime Player
2. File → New Screen Recording
3. Click record button (or Cmd+Control+Shift+4)
4. Select area or full screen
5. Click "Start Recording"
6. Follow this script
7. Click stop button in menu bar
8. File → Save
9. Upload to YouTube (unlisted) or Google Drive

---

## 🔧 If Recording with OBS Studio (Pro option):

1. Download from obsproject.com
2. Create new scene
3. Add "Display Capture" source
4. Add "Audio Input Capture" for microphone
5. Click "Start Recording"
6. Follow this script
7. Click "Stop Recording"
8. Video saved to default folder
9. Upload to platform of choice

---

## 📤 After Recording:

1. **Review the video**
   - Watch it once completely
   - Check audio quality
   - Verify all slides are visible
   - Ensure timing is under 5 minutes

2. **Re-record if needed**
   - Don't worry about being perfect
   - Focus on clarity and enthusiasm
   - 2-3 takes is normal

3. **Upload**
   - YouTube (unlisted) - best for sharing
   - Google Drive - with link sharing enabled
   - Loom - automatic hosting

4. **Add to README**
   - Edit main README.md
   - Add video link at the top
   - Format: `🎥 **[Watch Demo Video](your-link-here)**`

---

## 📧 Questions?

If you need help with:
- Recording tools setup
- Script modifications
- Technical issues
- Timing adjustments

Refer back to DEMO_GUIDE.md or reach out for support!

---

**Good luck with your recording! You've got this! 🚀**
