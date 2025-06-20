from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)

DATA_FILE = 'data.json'

def load_data():
    """Load JSON data from the data file."""
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    """Save JSON data to the data file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    """Render the homepage showing all events."""
    data = load_data()
    return render_template('index.html', events=data['events'])

@app.route('/create', methods=['GET', 'POST'])
def create_event():
    """Create a new event and save it to data.json."""
    if request.method == 'POST':
        data = load_data()
        event = {
            "id": len(data['events']) + 1,
            "name": request.form['name'],
            "type": request.form['type'],
            "date": request.form['date'],
            "location": request.form['location']
        }
        data['events'].append(event)
        save_data(data)
        return redirect(url_for('index'))
    return render_template('create_event.html')

@app.route('/register/<int:event_id>', methods=['GET', 'POST'])
def register(event_id):
    """Register a user for a specific event."""
    data = load_data()
    event = next((e for e in data['events'] if e['id'] == event_id), None)
    if request.method == 'POST':
        registration = {
            "event_id": event_id,
            "name": request.form['name'],
            "email": request.form['email'],
            "timestamp": str(datetime.now())
        }
        data['registrations'].append(registration)
        save_data(data)
        return redirect(url_for('index'))
    return render_template('register.html', event=event)

@app.route('/checkin/<int:event_id>', methods=['GET', 'POST'])
def checkin(event_id):
    """Check in a user to an event using their email."""
    data = load_data()
    if request.method == 'POST':
        checkin = {
            "event_id": event_id,
            "email": request.form['email'],
            "checkin_time": str(datetime.now())
        }
        data['checkins'].append(checkin)
        save_data(data)
        return redirect(url_for('index'))
    return render_template('checkin.html', event_id=event_id)

@app.route('/feedback/<int:event_id>', methods=['GET', 'POST'])
def feedback(event_id):
    """Submit feedback for a specific event."""
    if request.method == 'POST':
        data = load_data()
        fb = {
            "event_id": event_id,
            "rating": int(request.form['rating']),
            "comment": request.form['comment']
        }
        data['feedback'].append(fb)
        save_data(data)
        return redirect(url_for('index'))
    return render_template('feedback.html', event_id=event_id)

@app.route('/dashboard')
def dashboard():
    """Render the dashboard with summary stats and average feedback per event."""
    data = load_data()

    # Collect ratings grouped by event
    rating_summary = {}
    for fb in data.get('feedback', []):
        eid = fb['event_id']
        rating_summary.setdefault(eid, []).append(fb['rating'])

    # Compute average rating
    avg_ratings = {eid: sum(ratings) / len(ratings) for eid, ratings in rating_summary.items()}

    # Map event IDs to event names
    event_names = {event['id']: event['name'] for event in data['events']}

    return render_template(
        'dashboard.html',
        data=data,
        avg_ratings=avg_ratings,
        event_names=event_names
    )

@app.route('/delete/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    """Delete an event and its related data."""
    data = load_data()

    # Remove the event and associated data
    data['events'] = [event for event in data['events'] if event['id'] != event_id]
    data['registrations'] = [r for r in data.get('registrations', []) if r['event_id'] != event_id]
    data['checkins'] = [c for c in data.get('checkins', []) if c['event_id'] != event_id]
    data['feedback'] = [f for f in data.get('feedback', []) if f['event_id'] != event_id]

    save_data(data)
    return redirect(url_for('index'))

@app.route('/view_feedback/<int:event_id>')
def view_feedback(event_id):
    """View all feedback entries for a given event."""
    data = load_data()
    event = next((e for e in data['events'] if e['id'] == event_id), None)
    feedbacks = [f for f in data.get('feedback', []) if f['event_id'] == event_id]
    return render_template('view_feedback.html', event=event, feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
