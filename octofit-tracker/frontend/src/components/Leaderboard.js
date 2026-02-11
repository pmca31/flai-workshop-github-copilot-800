import React, { useState, useEffect } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
      console.log('Fetching from Leaderboard API endpoint:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Leaderboard data fetched:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      } catch (err) {
        console.error('Error fetching leaderboard:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
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
      <h2>🏆 Leaderboard</h2>
      <p className="text-muted mb-4">Top performers ranked by activity points</p>
      
      <div className="table-responsive">
        <table className="table table-hover">
          <thead>
            <tr>
              <th>Rank</th>
              <th>Name</th>
              <th>Email</th>
              <th>Team</th>
              <th>Total Points</th>
              <th>Last Updated</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length === 0 ? (
              <tr>
                <td colSpan="7" className="text-center">
                  <div className="alert alert-info" role="alert">
                    No leaderboard data available yet.
                  </div>
                </td>
              </tr>
            ) : (
              leaderboard.map((entry, index) => (
                <tr key={entry.id || index}>
                  <td>
                    {entry.rank === 1 && <span className="badge bg-warning text-dark">🥇 {entry.rank}</span>}
                    {entry.rank === 2 && <span className="badge bg-secondary">🥈 {entry.rank}</span>}
                    {entry.rank === 3 && <span className="badge bg-warning" style={{background: '#cd7f32'}}>🥉 {entry.rank}</span>}
                    {entry.rank > 3 && <span className="badge bg-info">{entry.rank}</span>}
                  </td>
                  <td><strong>{entry.user_name}</strong></td>
                  <td>{entry.user_email}</td>
                  <td><span className="badge bg-primary">{entry.team}</span></td>
                  <td><span className="badge bg-success">{entry.total_points} pts</span></td>
                  <td><small className="text-muted">{new Date(entry.updated_at).toLocaleDateString()}</small></td>
                  <td>
                    {entry.rank <= 3 ? (
                      <span className="badge bg-primary">Top 3</span>
                    ) : (
                      <span className="badge bg-secondary">Active</span>
                    )}
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Leaderboard;
