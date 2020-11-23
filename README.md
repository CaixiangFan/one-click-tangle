<h2 align="center">Tangle Deployment Tools</h2>

<p align="center">
  <a href="https://discord.iota.org/" style="text-decoration:none;"><img src="https://img.shields.io/badge/Discord-9cf.svg?logo=discord" alt="Discord"></a>
    <a href="https://iota.stackexchange.com/" style="text-decoration:none;"><img src="https://img.shields.io/badge/StackExchange-9cf.svg?logo=stackexchange" alt="StackExchange"></a>
    <a href="https://github.com/jmcanterafonseca-iota/IOTA-Tangle-Node-Deployment/blob/master/LICENSE" style="text-decoration:none;"><img src="https://img.shields.io/github/license/jmcanterafonseca-iota/IOTA-Tangle-Node-Deployment.svg" alt="MIT license"></a>
</p>
      
<p align="center">
  <a href="#about">About</a> ◈
  <a href="#prerequisites">Prerequisites</a> ◈
  <a href="#getting-started">Getting started</a> ◈
  <a href="#supporting-the-project">Supporting the project</a> ◈
  <a href="#joining-the-discussion">Joining the discussion</a> 
</p>

---

## About

This repository is where the IOTA Foundation hosts the open-source code for the [Tangle Explorer website](https://explorer.iota.org/).

The code is composed of:

- [**`api`:**](api/README.md) Handles functionality such as lookups for the client
- [**`client`:**](client/README.md) Provides a user interface for the explorer, using React.

These scripts are used when running Private Tangle instances through AWS [here](https://explorer-api.iota.org).

This is beta software, so there may be issues.
Please report any issues in our [issue tracker](https://github.com/iotaledger/explorer/issues/new).

## Prerequisites

To deploy your own version of the Tangle Explorer website, you need to have at least [version 10 of Node.js](https://nodejs.org/en/download/) installed on your device.

To check if you have Node.js installed, run the following command:

```bash
node -v
```

If Node.js is installed, you should see the version that's installed.

## Getting started

To get started, see the [deployment instructions](api/DEPLOYMENT.md).

## Supporting the project

If the Tangle Explorer website has been useful to you and you feel like contributing, consider submitting a [bug report](https://github.com/iotaledger/explorer/issues/new), [feature request](https://github.com/iotaledger/explorer/issues/new) or a [pull request](https://github.com/iotaledger/explorer/pulls/).

See our [contributing guidelines](.github/CONTRIBUTING.md) for more information.

## Joining the discussion

If you want to get involved in the community, need help with getting set up, have any issues or just want to discuss IOTA, Distributed Registry Technology (DRT), and IoT with other people, feel free to join our [Discord](https://discord.iota.org/).



# Tangle Deployment

A collection of recipes (docker, K8s manifests, scripts) to deploy public and private IOTA Nodes

