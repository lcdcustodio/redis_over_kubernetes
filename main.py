from flask import Flask
import redis
import datetime

app = Flask(__name__)

@app.route("/")
def hello():

    ct = datetime.datetime.now()
    r = redis.StrictRedis(host='redis-headless', port=6379, db=0)
    # Set a key-value pair
    #r.set('my_key', 'my_key')
    r.set('my_key', str(ct))

    # Get the value for a key
    value = r.get('my_key')
    print(value)  # Prints b'my_value'

    # Convert the value from bytes to string
    value_str = value.decode('utf-8')
    print(value_str)  # Prints 'my_value'

    return "Hello Redis. Getting value: " + value_str

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8080)