import random
import time

class InvalidResponseError(Exception):
    pass

def simulate_api_call():
    # Simulates a random API response
    responses = ['success', 'timeout', 'connection_error', 'invalid_response']
    return random.choice(responses)

def api_call_simulator():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        try:
            attempts += 1
            print(f"\nAttempt {attempts}...")
            time.sleep(1)  # Simulate delay

            response = simulate_api_call()

            if response == 'success':
                print(" API call succeeded.")
                break
            elif response == 'timeout':
                raise TimeoutError(" API call timed out.")
            elif response == 'connection_error':
                raise ConnectionError(" Could not connect to the server.")
            elif response == 'invalid_response':
                raise InvalidResponseError(" Received an invalid response from the API.")
        
        except (TimeoutError, ConnectionError, InvalidResponseError) as e:
            print(e)
            print("Retrying...")

        finally:
            print("Logged attempt:", attempts)

    else:
        print(" All API attempts failed. Please try again later.")

api_call_simulator()
