import React from 'react';

import './App.css';
import ChatBox from './components/ChatBox/ChatBox';



class App extends React.Component {

  componentDidMount() {
    const scriptElement = document.createElement('script');
    scriptElement.setAttribute('type', 'text/javascript');
    scriptElement.setAttribute('src', '__parcel_source_root/src/actions.js');

    document.body.appendChild(scriptElement);
  }

  render() {
    return (
      <div>
        <header className="App-header">
          Todo Application
        </header>
        <ChatBox />
      </div>
    )
  }
}


export default App
