import React, { useState } from 'react';

function App() {
  const [birthdate, setBirthdate] = useState('');
  const [daysSince, setDaysSince] = useState(null);
  const [error, setError] = useState('');

  const getDaysSinceBirth = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/days_since', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ birthdate: birthdate }),
      });

      const data = await response.json();
      if (data.error) {
        setError(data.error);
      } else {
        setDaysSince(data.days_since);
        setError('');
      }
    } catch (err) {
      setError('Failed to connect to the server');
    }
  };

  return (
    <div className="App">
      <h1>Days Since Birthdate</h1>
      <input
        type="date"
        value={birthdate}
        onChange={(e) => setBirthdate(e.target.value)}
      />
      <button onClick={getDaysSinceBirth}>Get Days Since</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {daysSince !== null && <p>Days since birth: {daysSince}</p>}
    </div>
  );
}

export default App;
