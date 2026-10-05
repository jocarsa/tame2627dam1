A septiembre de 2026, la versión LTSC actual es **Windows Server 2025**, disponible en **Standard** y **Datacenter**. Windows Server 2022 sigue soportado, pero su soporte estándar termina el 13 de octubre de 2026. ([Microsoft Learn][1])

### Windows Server 2025: requisitos mínimos

Microsoft establece estos mínimos para Windows Server 2025/Windows Server moderno: ([Microsoft Learn][2])

| Componente          | Requisito mínimo                                                  |
| ------------------- | ----------------------------------------------------------------- |
| CPU                 | **64 bits, 1,4 GHz**                                              |
| Instrucciones CPU   | x64, NX/DEP, CMPXCHG16b, LAHF/SAHF, PrefetchW, **SSE4.2, POPCNT** |
| Virtualización CPU  | **SLAT (EPT/NPT)**                                                |
| RAM Server Core     | **2 GB**                                                          |
| RAM con escritorio  | **2 GB**, Microsoft recomienda 4 GB                               |
| Disco               | **32 GB** mínimo                                                  |
| Red                 | **Ethernet 1 Gbit/s**                                             |
| Bus de red          | PCI Express                                                       |
| RAM servidor físico | ECC o tecnología similar                                          |
| Arquitectura        | exclusivamente **64 bits**                                        |

Los 32 GB son un **mínimo absoluto** y Microsoft advierte que puede ser necesario bastante más espacio dependiendo de RAM, actualizaciones y funciones instaladas. ([Microsoft Learn][2])

### Licencia

Aquí está la gran diferencia respecto a Windows 10/11: **la licencia puede costar bastante más que el ordenador**.

Microsoft licencia Windows Server 2025 Standard y Datacenter **por núcleos**, con un mínimo habitual de **16 cores licenciados por servidor**; además hacen falta **CAL** para los usuarios/dispositivos que accedan al servidor. ([Microsoft][3])

Como referencia española actual, Microsoft vende directamente **Windows Server 2025 Standard, 16 cores + 10 CAL por 1.978 €**. ([Microsoft][4])

En canal OEM/distribución se encuentran precios inferiores; por ejemplo, una lista de distribución española mostraba aproximadamente **780 € para Standard 2025 OEM 16 cores** y unos **4.542 € para Datacenter OEM 16 cores**, antes de considerar las CAL necesarias. ([Ingram Micro][5])

La diferencia fundamental es que Standard está pensado para servidores físicos o poco virtualizados y permite, con el licenciamiento correspondiente, **2 máquinas virtuales**, mientras que Datacenter permite **VM ilimitadas** sobre el host correctamente licenciado. ([Microsoft][3])

### ¿Cuánto cuesta el ordenador mínimo?

Curiosamente, **muy poco** si hablamos literalmente de satisfacer los requisitos y no de montar un servidor empresarial certificado.

Por ejemplo, actualmente aparecen equipos reacondicionados como:

### [HP ProDesk 400 G5 Intel Core i5-9500T]()

*195,08 €*

por aproximadamente **195 €**, con un i5-9500T que está enormemente por encima del mínimo de CPU.

También aparecen equipos de escritorio alrededor de **180–260 €**:

### [Dell OptiPlex 3060]()

*179,00 €*

### [Lenovo ThinkCentre M70s]()

*183,68 €*

### [HP ProDesk 400 G6 i5-10500T]()

*257,75 €*

Por tanto, para explicarlo en clase, yo resumiría los órdenes de magnitud así:

| Concepto                                                  |                       Windows Server 2025 |
| --------------------------------------------------------- | ----------------------------------------: |
| Hardware mínimo teórico                                   |                            **~150–250 €** |
| Hardware básico razonable (8–16 GB + SSD)                 |                            **~200–400 €** |
| Licencia Standard OEM 16 cores                            |       **~780 €** como referencia de canal |
| Standard 16 cores + 10 CAL, Microsoft                     |                               **1.978 €** |
| Datacenter 16 cores OEM                                   |     **~4.500 €** como referencia de canal |
| **Servidor básico + Standard**                            | desde aproximadamente **1.000 €** con OEM |
| **Servidor básico + Standard + 10 CAL oficial Microsoft** |                  alrededor de **2.200 €** |

Hay una distinción didáctica importante: **un PC de 200 € puede superar los requisitos técnicos mínimos de Windows Server 2025, pero eso no lo convierte en un servidor empresarial adecuado**. Para producción normalmente buscaríamos ECC, almacenamiento redundante/RAID, fuente fiable o redundante, más RAM, copias de seguridad y hardware específicamente soportado. Microsoft además señala expresamente ECC o tecnología equivalente para despliegues físicos. ([Microsoft Learn][2])

Si quieres, puedo hacerte a continuación una **tabla Windows 10 → Windows 11 → Server 2016 → 2019 → 2022 → 2025**, con **RAM, CPU, disco, precio de licencia y precio aproximado del hardware mínimo**, que puede quedar muy bien como material de clase.

[1]: https://learn.microsoft.com/es-es/windows/release-health/windows-server-release-info?utm_source=chatgpt.com "Información de versión de Windows Server | Microsoft Learn"
[2]: https://learn.microsoft.com/es-es/windows-server/get-started/hardware-requirements?utm_source=chatgpt.com "Requisitos de hardware para Windows Server | Microsoft Learn"
[3]: https://www.microsoft.com/es-es/windows-server/pricing?utm_source=chatgpt.com "Precios y licencias de Windows Server 2025 | Microsoft"
[4]: https://www.microsoft.com/es-es/d/windows-server-2025-standard/dg7gmgf0wzrw?utm_source=chatgpt.com "Comprar una licencia de Windows Server 2025 Standard (16 núcleos) y 5 o 10 CAL | Microsoft Store"
[5]: https://now.ingrammicro.com/rs/340-MXL-245/images/ES_ListaPreciosSemanal_MSFT_Update.pdf?version=4&utm_source=chatgpt.com "| LISTA DE PRECIOS - válida desde el 30 de Junio hasta el 4 de Julio del 2025  |  |  |  |"
