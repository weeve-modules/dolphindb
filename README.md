# DolphinDB

|           |                                                                           |
| --------- | ------------------------------------------------------------------------- |
| Name      | DolphinDB                                                                 |
| Version   | v1.0.0                                                                    |
| DockerHub | [weevenetwork/dolphindb](https://hub.docker.com/r/weevenetwork/dolphindb) |
| Authors   | Jakub Grzelak                                                             |

- [DolphinDB](#dolphindb)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Write data to your chosen DolphinDB table.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name             | Environment Variables | type    | Description                                                                                                                |
| ---------------- | --------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------- |
| Host             | HOST                  | string  | Host of DolphinDB server.                                                                                                  |
| Port             | PORT                  | integer | Port of DolphinDB server.                                                                                                  |
| Username         | USERNAME              | string  | Your DolphinDB username.                                                                                                   |
| Password         | PASSWORD              | string  | Your DolphinDB password.                                                                                                   |
| Database Path    | DB_PATH               | string  | Your database path.                                                                                                        |
| Table Name       | TABLE_NAME            | string  | Table to write data to.                                                                                                    |
| Database Columns | COLUMNS               | string  | List of comma (,) separated database columns headers to write to.                                                          |
| Data Labels      | LABELS                | string  | List of comma (,) separated labels in passed data. Order of labels must match the order of provided corresponding columns. |
| Date Column      | DATE_COLUMN           | string  | Name of column in database that holds date or timestamp (optional).                                                        |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
dolphindb
pandas
numpy
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "label-1": 12,
    "label-2": "speed"
}
```

* array of JSON body objects, example:

```json
[
    {
        "label-1": 12,
        "label-2": "speed"
    },
    {
        "label-1": 15,
        "label-2": "volume"
    }
]
```

## Output

Output of this module are records written to the selected DolphinDB table.
