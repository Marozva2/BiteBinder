import React from "react";

function Footer() {
  return (
    <footer className="ui inverted vertical footer segment">
      <div className="ui center aligned container">
        <div className="ui stackable inverted divided grid">
          <div className="three wide column">
            <h4 className="ui inverted header">Chefs</h4>
            <div className="ui inverted link list">
              <a href="#" className="item">
                Link One
              </a>
            </div>
          </div>
          <div className="three wide column">
            <h4 className="ui inverted header">Users</h4>
            <div className="ui inverted link list">
              <a href="#" className="item">
                Link Two
              </a>
            </div>
          </div>
          <div className="ten wide column">
            <p>
              Extra space for a call to action inside the footer that could help
              re-engage users.
            </p>
          </div>
        </div>
        <div className="ui inverted section divider"></div>
        <div className="ui horizontal inverted small divided link list">
          <a className="item" href="#">
            Site Map
          </a>
          <a className="item" href="#">
            Contact Us
          </a>
          <a className="item" href="#">
            Terms and Conditions
          </a>
          <a className="item" href="#">
            Privacy Policy
          </a>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
