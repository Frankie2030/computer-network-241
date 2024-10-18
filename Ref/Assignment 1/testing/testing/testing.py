import requests
import secrets
class TrackerClient:
    def __init__(self, tracker_url, torrent_info):
        self.tracker_url = tracker_url
        self.torrent_info = torrent_info

    def send_request(self, event, downloaded=0):        # tham số cho request parameter
        params = {
            'info_hash': self.torrent_info['info_hash'],
            'peer_id': self.torrent_info['peer_id'],
            'port': self.torrent_info['port'],
            'uploaded': self.torrent_info['uploaded'],
            'downloaded': downloaded,
            'left': self.torrent_info['left'],
            'event': event
        }
        # This line sends an HTTP GET request to the tracker server specified by self.tracker_url, 
        # with query parameters specified by the params dictionary.
        print(params)

        response = requests.get(self.tracker_url, params=params)
        
        return response.text

    def parse_response(self, response):
        response_dict = dict(item.split('=') for item in response.split('&'))
        if 'failure reason' in response_dict:
            print("Tracker Error:", response_dict['failure reason'])
        elif 'warning message' in response_dict:
            print("Tracker Warning:", response_dict['warning message'])
        else:
            tracker_id = response_dict.get('tracker id', None)
            peers = []
            for key in response_dict:
                if key.startswith('peer '):
                    peer_info = response_dict[key].split(':')
                    peer = {'peer id': peer_info[0], 'ip': peer_info[1], 'port': int(peer_info[2])}
                    peers.append(peer)
            print("Tracker ID:", tracker_id)
            print("Peers:", peers)

# Example usage:
tracker_url = 'http://tracker.example.com:8080/announce'
torrent_info = {
    'info_hash': 'abcdef1234567890',
    'peer_id': '-TR' + ''.join(secrets.choice('1234567890abcdef') for _ in range(20 - len('-TR'))),
    'port': 6881,
    'uploaded': 0,
    'left': 1000000  # Total file size in bytes
}

tracker_client = TrackerClient(tracker_url, torrent_info)
response = tracker_client.send_request('started', downloaded=0)
tracker_client.parse_response(response)
