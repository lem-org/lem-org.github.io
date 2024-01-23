---
title: 'What is Application Performance Monitoring(APM)?'
authors:
  - "wu_hong"
---

If your team is facing the following pain points regarding system performance:

- Manual monitoring of system performance after release is required.
- Troubleshooting performance issues is proving to be difficult.

Application performance monitoring(APM) tools could potentially alleviate these pain points for you.

## I. The fundamental idea of APM

Most of the APM systems on the market are essentially modeled after Google's [Dapper](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/), a tracing system for large-scale distributed systems. You could find more information [here](https://github.com/gg-daddy/ebooks/blob/master/Google%20Dapper.pdf).

The fundamental idea of APM is to record and propagate an application-level tag when services interact with each other, which can be used to establish relationships between different service nodes. For instance, if HTTP is used as the request protocol between two nodes, these tags will be included in the HTTP headers. Thus, how to propagate these tags depends on the communication protocol used between nodes.

## II. What kind of value that the APM could provide us?

APM offers businesses several benefits:

#### 1. Customer satisfaction

APM could help us ensure services/systems meet technological performance standards to provide customers with a quality user experience.

It enables real-time monitoring and diagnosis of application performance and health. By monitoring key metrics like the average response time, request rate, CPU usage, error rates, and other key metrics of systems, we can promptly identify and resolve potential performance issues and failures, ensuring the stability and reliability of the application.

#### 2. Performance optimization & Rapid diagnosis

APM helps us gain in-depth insights into performance bottlenecks and their root causes. By analyzing performance metrics and transaction tracing data, we can identify the sources of performance issues and optimize them accordingly, improving application response time and throughput for a better user experience.

#### 3. Capacity planning and resource management

We could use APM tools to determine how much resource, infrastructure, and computing power is necessary to keep applications performing optimally. This keeps operating costs to a minimum.

## III. Key considerations for selecting an APM tool

#### 1. Integration cost of the APM tool

- Technology stack support.
    > Ensure that the selected APM tool is compatible with your current technology stack, enabling accurate monitoring and analysis of your application.
- Intrusiveness into source code and configuration files.
    > Consider whether modifications to the application's source code or configuration files are required for integrating the APM tool. Opt for tools with minimal intrusiveness to reduce modifications to existing code and configurations.
- APM system maintenance cost.
    > Evaluate the operational cost associated with the APM system of the chosen tool, including installation, configuration, maintenance, and upgrades. Ensure that you have sufficient resources and technical capabilities to manage and maintain the APM system.

#### 2. Provision of required monitoring data

- Coverage of monitoring data.
    > Ensure that the selected APM tool provides the required monitoring data, including performance metrics, transaction tracing, error diagnostics, etc. Based on your application's needs, verify if the tool offers sufficiently detailed monitoring data to meet your requirements.
- Customization of monitoring and alerts.
    > Consider whether the tool supports customization of monitoring metrics and alert rules. This allows you to tailor monitoring and alerts based on specific needs of your application, better aligning with your business requirements.

## IV. What APM tools are available in the IT industry?

[New Relic](https://newrelic.com/) is one of the top performers in the commercial APM SaaS service category, while [SkyWalking](https://github.com/apache/skywalking) and [Pinpoint](https://github.com/pinpoint-apm/pinpoint) are considered the best open-source APM tools.
