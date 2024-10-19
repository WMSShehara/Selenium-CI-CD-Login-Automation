'use client'
import React, { useState } from 'react'

const LoginForm = () => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = e => {
    e.preventDefault()
    console.log('Username:', username)
    console.log('Password:', password)
  }

  return (
    <div style={styles.container}>
      <h2 style={styles.heading}>Login</h2>
      <form onSubmit={handleSubmit} style={styles.form}>
        <div style={styles.inputContainer}>
          <label>Username:</label>
          <input
            type='text'
            name='username'
            value={username}
            onChange={e => setUsername(e.target.value)}
            required
            style={styles.input}
          />
        </div>
        <div style={styles.inputContainer}>
          <label>Password:</label>
          <input
            type='password'
            name='password'
            value={password}
            onChange={e => setPassword(e.target.value)}
            required
            style={styles.input}
          />
        </div>
        <button type='submit' style={styles.button} xpath='button'>
          Login
        </button>
      </form>
    </div>
  )
}

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: '#f7f7f7'
  },
  heading: {
    marginBottom: '20px',
    color: '#333'
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    width: '300px',
    padding: '20px',
    boxShadow: '0px 4px 6px rgba(0, 0, 0, 0.1)',
    backgroundColor: 'white',
    borderRadius: '8px'
  },
  inputContainer: {
    marginBottom: '15px'
  },
  input: {
    width: '100%',
    padding: '10px',
    borderRadius: '4px',
    border: '1px solid #ccc',
    outline: 'none',
    transition: 'border 0.3s'
  },
  inputFocus: {
    borderColor: '#007BFF'
  },
  button: {
    padding: '10px',
    backgroundColor: '#007BFF',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    transition: 'background-color 0.3s'
  }
}

export default LoginForm
