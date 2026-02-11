import React, { useState, useEffect } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
      console.log('Fetching from Workouts API endpoint:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Workouts data fetched:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching workouts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-spinner">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="error-message">
        <strong>Error:</strong> {error}
      </div>
    </div>
  );

  return (
    <div className="container mt-4">
      <h2>💪 Workouts</h2>
      <p className="text-muted mb-4">Personalized workout suggestions for your fitness journey</p>
      
      {workouts.length === 0 ? (
        <div className="alert alert-info" role="alert">
          No workouts available at the moment.
        </div>
      ) : (
        <div className="row">
          {workouts.map((workout) => (
            <div key={workout.id} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-header">
                  <h5 className="mb-0">{workout.name || workout.title}</h5>
                </div>
                <div className="card-body">
                  <p className="card-text">{workout.description}</p>
                  <div className="mb-2">
                    <strong>Difficulty:</strong>{' '}
                    {workout.difficulty_level === 'Beginner' || workout.difficulty === 'Beginner' ? (
                      <span className="badge bg-success">{workout.difficulty_level || workout.difficulty}</span>
                    ) : workout.difficulty_level === 'Intermediate' || workout.difficulty === 'Intermediate' ? (
                      <span className="badge bg-warning text-dark">{workout.difficulty_level || workout.difficulty}</span>
                    ) : (
                      <span className="badge bg-danger">{workout.difficulty_level || workout.difficulty}</span>
                    )}
                  </div>
                  <div className="mb-2">
                    <strong>Duration:</strong> <span className="badge bg-info">{workout.duration} min</span>
                  </div>
                  <div className="mb-3">
                    <strong>Category:</strong> {workout.category || 'General'}
                  </div>
                  <button className="btn btn-primary w-100">Start Workout</button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Workouts;
