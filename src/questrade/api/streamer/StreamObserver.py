'''Stream Observer

@summary: An Observer in the Publish/Subscriber design pattern.  This
    observer prints the JSON object returned from the stream.

@see: http://www.questrade.com/api/documentation/streaming

@copyright: 2016
@author: Peter Cinat
@license: Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

from Observer import Observer
import json

class StreamObserver(Observer):
    
    def update(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            s = payload.decode('utf8')
            try:
                j = json.loads(s)
                print j
            except ValueError:
                print s
        