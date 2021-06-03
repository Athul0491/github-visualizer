/** @format */

import React, { useState, useEffect } from 'react';
import axios from 'axios';

// kaunsa code?
// v
const Data = ({ username, repository }) => {
  const [git_data, setGit_data] = useState({});

  useEffect(() => {
    axios
      .post(`http://127.0.0.1:5000/github`, [username, repository])
      .then(res => {
        console.log(res.data);
        setGit_data(res.data);
      });
  }, []);

  return (
    <div>
      <h1>Hello world</h1>
      {/* {git_data.map(git_data => (
        <li>{git_data.name}</li>
      ))} */}
    </div>
  );
};

export default Data;
