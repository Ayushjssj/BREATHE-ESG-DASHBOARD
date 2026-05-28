import { useEffect, useMemo, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [activities, setActivities] = useState([]);
  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState("ALL");
  const [currentTime, setCurrentTime] = useState(new Date().toLocaleString());

  useEffect(() => {
    fetchActivities();

    const timer = setInterval(() => {
      setCurrentTime(new Date().toLocaleString());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  const fetchActivities = async () => {
    const response = await axios.get("http://127.0.0.1:8000/api/activities/");
    setActivities([...response.data].sort((a, b) => a.id - b.id));
  };

  const approveActivity = async (id) => {
    await axios.post(`http://127.0.0.1:8000/api/activities/${id}/approve/`);
    fetchActivities();
  };

  const lockActivity = async (id) => {
    await axios.post(`http://127.0.0.1:8000/api/activities/${id}/lock/`);
    fetchActivities();
  };

  const filteredActivities = useMemo(() => {
    return activities.filter((item) => {
      const text = `${item.activity_type} ${item.source_type} ${item.scope}`.toLowerCase();
      const matchesSearch = text.includes(search.toLowerCase());
      const matchesStatus = statusFilter === "ALL" || item.status === statusFilter;
      return matchesSearch && matchesStatus;
    });
  }, [activities, search, statusFilter]);

  const totalCount = activities.length;
  const pendingCount = activities.filter((a) => a.status === "PENDING").length;
  const approvedCount = activities.filter((a) => a.status === "APPROVED").length;
  const lockedCount = activities.filter((a) => a.status === "LOCKED").length;

  return (
    <div className="app">
      <div className="dashboard">
        <div className="header">
          <div className="brand">
            <div className="logo">🌿</div>
            <div>
              <p>ENTERPRISE ESG REVIEW PLATFORM</p>
              <h1>BREATHE ESG DASHBOARD</h1>
              <span className="time">{currentTime}</span>
            </div>
          </div>

          <button className="refreshBtn" onClick={fetchActivities}>
            ↻ Refresh
          </button>
        </div>

        <div className="kpiGrid">
          <div className="kpiCard total">
            <div className="icon blue">▰</div>
            <div>
              <p>TOTAL ACTIVITIES</p>
              <h2>{totalCount}</h2>
            </div>
          </div>

          <div className="kpiCard pendingCard">
            <div className="icon yellow">◔</div>
            <div>
              <p>PENDING COUNT</p>
              <h2>{pendingCount}</h2>
            </div>
          </div>

          <div className="kpiCard approvedCard">
            <div className="icon green">✓</div>
            <div>
              <p>APPROVED COUNT</p>
              <h2>{approvedCount}</h2>
            </div>
          </div>

          <div className="kpiCard lockedCard">
            <div className="icon red">🔒</div>
            <div>
              <p>LOCKED COUNT</p>
              <h2>{lockedCount}</h2>
            </div>
          </div>
        </div>

        <div className="toolbar">
          <input
            type="text"
            placeholder="🔍  Search by activity, source, or scope..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />

          <select value={statusFilter} onChange={(e) => setStatusFilter(e.target.value)}>
            <option value="ALL">All Status</option>
            <option value="PENDING">Pending</option>
            <option value="APPROVED">Approved</option>
            <option value="LOCKED">Locked</option>
          </select>
        </div>

        <div className="tableCard">
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Activity</th>
                <th>Source</th>
                <th>Scope</th>
                <th>Quantity</th>
                <th>Unit</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>

            <tbody>
              {filteredActivities.map((activity) => (
                <tr key={activity.id}>
                  <td>{activity.id}</td>
                  <td>{activity.activity_type}</td>
                  <td>{activity.source_type}</td>
                  <td>{activity.scope}</td>
                  <td>{activity.normalized_quantity}</td>
                  <td>{activity.normalized_unit}</td>
                  <td>
                    <span className={`status ${activity.status.toLowerCase()}`}>
                      {activity.status}
                    </span>
                  </td>
                  <td>
                    <button
                      className="approveBtn"
                      disabled={activity.status === "LOCKED"}
                      onClick={() => approveActivity(activity.id)}
                    >
                      Approve
                    </button>

                    <button
                      className="lockBtn"
                      disabled={activity.status === "LOCKED"}
                      onClick={() => lockActivity(activity.id)}
                    >
                      Lock
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          {filteredActivities.length === 0 && (
            <p className="empty">No matching activities found.</p>
          )}
        </div>

        <div className="footer">
          Built by Ayush Pandey • ESG Monitoring Platform
        </div>
      </div>
    </div>
  );
}

export default App;