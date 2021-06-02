import React, { Component } from "react";
import axios from "axios";

export default class Data extends Component {
  state = {
    git_data: [],
  };
  componentDidMount() {
    axios
      .get("http://127.0.0.1:5000/github", username, repository)
      .then((res) => {
        const git_data = res.data;
        this.setState({ git_data });
      });
  }
  render() {
    return (
      <div>
        {this.state.git_data.map((git_data) => (
          <li>{git_data.name}</li>
        ))}
      </div>
    );
  }
}
