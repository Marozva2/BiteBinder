import React, { useState } from 'react';
import { Button, Form, Grid, Header, Message, Segment } from 'semantic-ui-react';

function Authentication({ onSignIn, onSignUp }) {
  const [isSigningIn, setIsSigningIn] = useState(true);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleToggle = () => {
    setIsSigningIn(!isSigningIn);
  };

  const handleSubmit = () => {
    if (isSigningIn) {
      onSignIn(username, password);
    } else {
      onSignUp(username, password);
    }
  };

  return (
    <Grid textAlign='center' style={{ height: '100vh' }} verticalAlign='middle'>
      <Grid.Column style={{ maxWidth: 450 }}>
        <Header as='h2' color='teal' textAlign='center'>
          {isSigningIn ? 'Log-in to your account' : 'Sign-up for an account'}
        </Header>
        <Form size='large' onSubmit={handleSubmit}>
          <Segment stacked>
            <Form.Input 
              fluid icon='user' 
              iconPosition='left' 
              placeholder='Username' 
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <Form.Input
              fluid
              icon='lock'
              iconPosition='left'
              placeholder='Password'
              type='password'
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <Button color='teal' fluid size='large'>
              {isSigningIn ? 'Sign In' : 'Sign Up'}
            </Button>
          </Segment>
        </Form>
        <Message>
          {isSigningIn ? 'New to us? ' : 'Already have an account? '}
          <Button onClick={handleToggle}>
            {isSigningIn ? 'Sign Up' : 'Sign In'}
          </Button>
        </Message>
      </Grid.Column>
    </Grid>
  );
}

export default Authentication;
