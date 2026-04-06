
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  return (
    <div>
      {/* Bootstrap Navigation */}
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">OctoFit Tracker</a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Activities</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Teams</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Leaderboard</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container mt-5">
        {/* Bootstrap Heading */}
        <h1 className="display-4 mb-4 text-center">Welcome to OctoFit Tracker</h1>

        {/* Bootstrap Card Example */}
        <div className="row justify-content-center">
          <div className="col-md-6">
            <div className="card shadow">
              <div className="card-body">
                <h5 className="card-title">Get Started</h5>
                <p className="card-text">Track your fitness activities, join teams, and climb the leaderboard!</p>
                <a href="#" className="btn btn-primary">View Activities</a>
              </div>
            </div>
          </div>
        </div>

        {/* Bootstrap Table Example */}
        <div className="row mt-5">
          <div className="col">
            <h2 className="mb-3">Sample Leaderboard</h2>
            <table className="table table-striped table-bordered">
              <thead className="table-dark">
                <tr>
                  <th>Rank</th>
                  <th>User</th>
                  <th>Points</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td>Alice</td>
                  <td>1200</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>Bob</td>
                  <td>1100</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>Charlie</td>
                  <td>950</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        {/* Bootstrap Button Example */}
        <div className="row mt-4">
          <div className="col text-center">
            <button className="btn btn-success me-2">Join Team</button>
            <button className="btn btn-outline-secondary">Log Activity</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
