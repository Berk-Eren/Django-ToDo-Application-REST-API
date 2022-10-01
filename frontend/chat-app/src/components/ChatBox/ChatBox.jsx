import React from "react"
import './ChatBox.css';
import { useState } from 'react';


function ChatBox() {
  const [user, setUser] = useState("admin");
  const [isOnline, setIsOnline] = useState(true);

  return (
    <div>
      <div className="fabs">
        <div className="chat">
          <div className="chat_header">
            <div className="chat_option">
              <div className="header_img">
                <img
                  src="./profilePic.jpg"
                />
              </div>
              <span id="chat_head">{user}</span> <br />
              <span className="online">{isOnline ? "Online": "Offline"}</span>
              <span id="chat_fullscreen_loader" className="chat_fullscreen_loader"
              ><i className="fullscreen zmdi zmdi-window-maximize"></i
              ></span>
            </div>
          </div>
          <div id="chat_converse" className="chat_conversion chat_converse">
          </div>
          <div className="fab_field">
            <a id="fab_camera" className="fab"><i className="zmdi zmdi-camera"></i></a>
            <a id="fab_send" className="fab"><i className="zmdi zmdi-mail-send"></i></a>
            <textarea
              id="chatSend"
              name="chat_message"
              placeholder="Send a message"
              className="chat_field chat_message"
            ></textarea>
          </div>
        </div>
        <a id="prime" className="fab"
        ><i className="prime zmdi zmdi-comment-outline"></i
        ></a>
      </div>
    </div>
  )
}

export default ChatBox
