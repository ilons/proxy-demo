import React from 'react';
import logo from './logo.svg';
import './App.css';

class RequestInfo extends React.Component {
    render() {
        console.log('Render request info..', this);
        return (
            <div>
                <p>Request..</p>
            </div>
        );
    }
}

function App() {
  return (
    <div className="App">
      <RequestInfo/>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;