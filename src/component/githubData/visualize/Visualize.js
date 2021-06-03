/** @format */

import React, { useState } from 'react';
import Data from './Data';

function Visualize() {
  const [input1, setInput1] = useState('');
  const [input2, setInput2] = useState('');
  const [showData, setShowData] = useState(false);

  const handleChangeU = e => {
    setInput1(e.target.value);
  };
  const handleChangeR = e => {
    setInput2(e.target.value);
  };
  const handleSubmit = e => {
    setShowData(false);
    e.preventDefault();
    console.log(input1, input2);
    setInput1('');
    setInput2('');
    setShowData(true);
  };
  return (
    <div className='center'>
      <div className='title'>Github Details</div>
      <div className='sub_title'>Get details about github repositories</div>
      <form className='form' onSubmit={handleSubmit}>
        <div className='btns'>
          <input
            type='text'
            placeholder='Username'
            value={input1}
            onChange={handleChangeU}
          ></input>
          <input
            type='text'
            placeholder='Repository'
            value={input2}
            onChange={handleChangeR}
          ></input>
          <button>Search</button>
        </div>
      </form>
      {showData ? <Data username={input1} repository={input2} /> : ''}
    </div>
  );
}

export default Visualize;
