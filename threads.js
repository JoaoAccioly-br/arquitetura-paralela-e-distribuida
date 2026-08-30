const { Worker, isMainThread, parentPort } = require('worker_threads')


if (isMainThread){
    console.log("duas mensagens em paralelo.");

    const worker = new Worker(__filename);

    // Before Worker

    console.log("teste02 - sem esperar worker");

    worker.on('message', (msg) => console.log(msg));

    worker.on('exit', () => console.log('exit!'));
} else {
    setTimeout(() => {
        parentPort.postMessage("executing in parallel");
    }, 0);
}
