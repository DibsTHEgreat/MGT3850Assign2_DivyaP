
# 📅 Event Management Dashboard (Flask App)

## Author

Divya Pateliya  
Student at University of Lethbridge
MGT3850 - Assignment 2

---

## Overview

This is a simple web application built with Flask to manage events, registrations, check-ins, feedback collection, and visual analytics. It’s designed to simulate a basic event hosting platform with CRUD capabilities and data visualization.

## 💼 Business Problem

**Problem:**  
Event organizers often struggle to efficiently manage the end-to-end process of hosting events, including collecting registrations, tracking attendance, gathering feedback, and analyzing event success. These processes are frequently handled through separate tools (e.g., spreadsheets, email forms), leading to disorganization, duplicated work, and lack of real-time insights.

**Why it Matters:**  
For small businesses, educational institutions, or community groups that host recurring events, a lack of centralized event management and data tracking can lead to lower attendance, poor feedback collection, and missed opportunities to improve future events.

**Solution:**  
This Flask-based web application provides a streamlined platform to:
- Create and manage events  
- Register attendees and track check-ins  
- Collect and view feedback  
- Visualize event performance using charts (e.g., average ratings)

By consolidating all these tasks into one interface and supporting data visualization, the application helps organizers make informed decisions, improve attendee experiences, and reduce administrative overhead.

---

## Features

- ✅ Create and list events
- 📝 Register participants for events
- 🔐 Event check-in tracking
- 💬 Submit and view feedback
- 📊 Dashboard with real-time event metrics and average feedback ratings using Chart.js
- ❌ Delete events and clean up associated data

---

## Tech Stack

- Python 3.x
- Flask
- HTML/CSS (Jinja2 Templates)
- JSON (as a data store)
- Chart.js (for data visualization)

---

## Installation

1. Clone or download this repository.
2. Install dependencies:

```bash
pip install flask
```

3. Run the app:

```bash
python app.py
```

4. Open your browser and go to:  
   `http://localhost:5000`

---

## File Structure

```
├── app.py
├── data.json
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── create_event.html
│   ├── register.html
│   ├── checkin.html
│   ├── feedback.html
│   ├── dashboard.html
│   └── view_feedback.html
├── static/
│   └── style.css
├── README.md
```

---

## Usage

1. **Homepage** `/` - View all events  
2. **Create Event** `/create` - Add new events  
3. **Register** `/register/<event_id>` - Sign up participants  
4. **Check-in** `/checkin/<event_id>` - Mark attendance  
5. **Feedback** `/feedback/<event_id>` - Submit feedback  
6. **Dashboard** `/dashboard` - See stats and visualizations  
7. **View Feedback** `/view_feedback/<event_id>` - View feedback for a specific event  
8. **Delete** `/delete/<event_id>` - Remove event and data (POST only)

---

## Testing

- Manual testing was done for:
  - Event creation, registration, check-in, feedback
  - Edge cases like deleting non-existent events, empty feedback, etc.
---

## License

MIT License (Free to use, modify, distribute)
