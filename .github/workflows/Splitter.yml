addEventListener(
  "fetch", event => {
      let url = new URL(event.request.url);
      let realhostname = url.pathname.split('/')[2];
      let realpathname = url.pathname.split('/')[1];
      url.hostname = realhostname;
      url.pathname = '/'+ realpathname;
      url.protocol = "https";
      let request = new Request(url, event.request);
      event.respondWith(
         fetch(request)
      )
  }
)
