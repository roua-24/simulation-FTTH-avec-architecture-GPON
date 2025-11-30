**Simulation d’un réseau FTTH avec architecture GPON**
Projet de stage  – Août 2025
Auteur : Roua Jendoubi

 ****Description du projet****

Ce projet consiste à simuler un réseau FTTH (Fiber To The Home) basé sur l’architecture GPON (Gigabit Passive Optical Network).
Il inclut :

La modélisation des composants du réseau optique (OLT, ONT, splitters, fibre)

La simulation réseau (connectivité, QoS, pannes)

La supervision via SNMP

L’analyse du trafic et des performances (latence, jitter, bande passante)

L’automatisation avec Python + SQLite (supervision, budget optique)

Le travail a été réalisé dans le cadre d’un stage au sein de SOTETEL, un leader tunisien spécialisé dans les infrastructures télécoms.

****Objectifs principaux****

Concevoir une topologie FTTH/GPON complète

Configurer les équipements réseau (VLAN, DHCP, VoIP…)

Simuler différents scénarios réseau :

Téléchargement de fichier

Panne fibre + alertes LOS/LOF

Tests QoS (VoIP, vidéo, data)

Montée en charge

Mettre en place un système de supervision SNMP avec stockage SQLite

Automatiser les calculs de budget optique via Python

**Architecture GPON simulée**

OLT (Optical Line Terminal)

Splitter 1:N

ONT (Optical Network Terminal)

ODN (Optical Distribution Network)

Longueurs d’onde :

1490 nm (downstream)

1310 nm (upstream)

1550 nm (RF vidéo)

**Outils utilisés**
  **Simulation réseau**

Cisco Packet Tracer

GNS3

Wireshark

  ****Supervision & Automatisation****

SNMP (supervision des équipements IP)

Python (collecte automatique, budget optique)

SQLite (base de données de supervision)

Graphviz (schémas d’architecture)

****Scénarios simulés**** 
1. Téléchargement de fichier

→ Stabilité du débit, latence faible, pertes négligeables.

2. Panne fibre + alarmes LOS/LOF

→ Détection immédiate, perte totale de connectivité, supervision fonctionnelle.

3. Tests QoS (VoIP, vidéo, data)

→ Priorisation correcte des flux sensibles (VoIP & vidéo).
→ Réduction du jitter & latence avec QoS activée.

4. Montée en charge

→ Maintien de la connectivité avec légère dégradation sous forte charge.

5. VoIP sur GPON

→ Appels entre deux IP Phones via ONT : réussi.

6. Budget optique (Python)

→ Analyse des scénarios 1:32 et 1:64.
→ Baisse de la marge optique avec ratio élevé.

****Résultats globaux****

Configuration cohérente et stable

QoS efficace pour les services critiques

SNMP + SQLite = supervision centralisée et fiable

Réseau performant même sous charge

Simulation pertinente malgré les limites de GNS3/Packet Tracer pour les protocoles GPON réels

****Perspectives d’amélioration****

Intégrer une interface graphique de supervision

Ajouter un système d’alertes automatiques (mail, notifications)

Passer vers un banc GPON réel ou émulateur professionnel

Utiliser des outils modernes comme Grafana / Zabbix pour la visualisation

****Contenu du dépôt GitHub****
├── Rapport_de_stage_FTTH_GPON.pdf

├── scripts/

│   ├── snmp_collector.py

│   ├── budget_optique.py

│   └── sql_structure.sql

├── configurations/

│   ├── cisco_packet_tracer/

│   ├── gns3/

│   └── qos_voip/

├── graphviz/

│   ├── snmp_flows.gv

│   ├── omci_flows.gv

│   └── snmp_vs_omci.gv

└── README.md


****Auteur****

Roua Jendoubi
Étudiante en télécommunications & réseaux
Passionnée par les technologies optiques, la simulation réseau et la cybersécurité.

****Licence****

Ce projet est partagé à des fins éducatives dans le cadre d’un stage académique.
Toute réutilisation doit citer l’auteure et la source.
