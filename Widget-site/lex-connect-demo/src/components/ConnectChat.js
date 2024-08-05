// src/components/ConnectChat.js
import { useEffect } from 'react';

const ConnectChat = () => {
  useEffect(() => {
    const script = document.createElement('script');
    script.src = 'https://dtn7rvxwwlhud.cloudfront.net/amazon-connect-chat-interface-client.js';
    script.async = true;
    script.id = 'adaf3036-dde0-46ea-802d-5871b13c06b4';
    document.head.appendChild(script);

    script.onload = () => {
      window.amazon_connect = window.amazon_connect || function() {
        (window.amazon_connect.ac = window.amazon_connect.ac || []).push(arguments);
      };
      window.amazon_connect('styles', {
        iconType: 'CHAT',
        openChat: { color: '#ffffff', backgroundColor: '#122854' },
        closeChat: { color: '#ffffff', backgroundColor: '#123456'}
      });
      window.amazon_connect('snippetId', 'QVFJREFIaWFZYXRVSlpIekdkUUg5YXhZenVQMktKRXNIWTVFQWpBYVErTEdzRnpvZHdIcTFpM0QwY3RDdU1ydUFEejZkUFBuQUFBQWJqQnNCZ2txaGtpRzl3MEJCd2FnWHpCZEFnRUFNRmdHQ1NxR1NJYjNEUUVIQVRBZUJnbGdoa2dCWlFNRUFTNHdFUVFNQnBwVkIyUDN2MmRtclp3bUFnRVFnQ3VDQ2Nxem40TzFxQmZRYWxzU2MvbzQzZk9pS1MrREFEeHdZOVVXOWNwNjdycXlmZTJHU3p1M2JROGg6OmYzUmNyZW9Pa2FjV1h4NkU4V3NhSENTM01MN0lRRHBCblFFVE4vbkorRWZKZ2lzTy94Q25BNzJvVHBhb0VTZUdjdFVvYjBwK1lQbHdneTMya0dNSSt5SWFJUGhxQkNqWnpULzY3eWVpRzFTam81dWtkY0txQUFQUzBhSjBWNjBtcjBuVHBCb3NhNVhCRHByUEJQbm9zUHZlRm9ZdkdiTT0=');
      window.amazon_connect('supportedMessagingContentTypes', [
        'text/plain', 'text/markdown', 
        'application/vnd.amazonaws.connect.message.interactive', 
        'application/vnd.amazonaws.connect.message.interactive.response'
      ]);
    };

    return () => {
      document.getElementById('adaf3036-dde0-46ea-802d-5871b13c06b4')?.remove();
    };
  }, []);

  return null; // This component does not render anything itself
};

export default ConnectChat;
