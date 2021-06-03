/** @format */

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Data = () => {
  const [git_data, setGit_data] = useState({});

  useEffect(() => {
    axios
      .get('http://127.0.0.1:5000/github', username, repository)
      .then(res => {
        const git_data = res.data;
        setGit_data(git_data);
      });
  }, []);

  return (
    <div>
      {this.state.git_data.map(git_data => (
        <li>{git_data.name}</li>
      ))}
    </div>
  );
};

export default Data;
