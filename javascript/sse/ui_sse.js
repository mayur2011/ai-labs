// Open a persistent connection to the server stream
const eventSource = new EventSource("http://localhost:8001/stream-events");

// Listen for incoming tokens ("bricks")
eventSource.onmessage = function(event) {
    console.log("New token received:", event.data);
    // Logic to update your UI "brick-by-brick" goes here
};

// Gracefully handle errors or disconnection
eventSource.onerror = function(error) {
    console.error("EventSource failed:", error);
    eventSource.close(); 
};