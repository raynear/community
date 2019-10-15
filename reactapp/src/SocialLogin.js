import React, { Component } from "react";

import {
  STATUS,
  Loading,
  Avatar,
  Logo,
  Logotype,
  Container,
  Header
} from "gitstar-components";

const CLIENT_ID = "cdc18a1912950f105f70";
const REDIRECT_URI = "http://localhost:3000/";

class SocialLogin extends Component {
  constructor(props) {
    super(props);
    this.state = {
      status: STATUS.INITIAL,
      token: null
    };
  }

  render() {
    return (
      <a
        href={`https://github.com/login/oauth/authorize?client_id=${CLIENT_ID}&scope=user&redirect_uri=${REDIRECT_URI}`}
      >
        Login
      </a>
    );
  }
}

export default SocialLogin;
