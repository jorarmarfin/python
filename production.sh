#!/bin/bash
echo 'Ingresar opcion limpia Cache(lc), Copia archivos files(cf),copia modulos(cm), crear usuarios (cu), elimina usuarios (eu)'
read opcion 
case $opcion in
     lc)
        docker exec -it srv-cuenca-pampas-apache drupal cr
        docker exec -it srv-cuenca-chanchay-lambayeque-apache drupal cr
        docker exec -it srv-cuenca-urubamba-apache drupal cr
        docker exec -it srv-cuenca-mayo-apache drupal cr
        docker exec -it srv-cuenca-jequetepeque-zana-apache drupal cr
        docker exec -it srv-cuenca-mantaro-apache drupal cr
        docker exec -it srv-cuenca-quilca-chili-apache drupal cr
        docker exec -it srv-cuenca-atlantico-apache drupal cr
        docker exec -it srv-cuenca-chancay-huaral-apache drupal cr
        docker exec -it srv-cuenca-pacifico-apache drupal cr
        docker exec -it srv-cuenca-caplina-locumba-apache drupal cr
        docker exec -it srv-cuenca-chira-piura-apache drupal cr
        docker exec -it srv-cuenca-tumbes-apache drupal cr
        docker exec -it srv-cuenca-chira-piura-apache drupal cr
          ;;
     cm)
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules caplina-locumba/www/web/modules/custom
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules chancay-huaral/www/web/modules/custom
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules chanchay-lambayeque/www/web/modules/custom
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules chillon-rimac-lurin/www/web/modules/custom
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules chira-piura/www/web/modules/custom
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules jequetepeque-zana/www/web/modules/custom
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules mantaro/www/web/modules/custom
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules mayo/www/web/modules/custom
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules pampas/www/web/modules/custom
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules quilca-chili/www/web/modules/custom
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules tumbes/www/web/modules/custom
        cp -rf pacifico/www/web/modules/custom/drinux_event_modules urubamba/www/web/modules/custom
        cp -rf pacifico/www/web/sites/default/files caplina-locumba/www/web/sites/default
        echo 'modulos copiados'
          ;;
     cf)
        cp -rf pacifico/www/web/sites/default/files chancay-huaral/www/web/sites/default
        cp -rf pacifico/www/web/sites/default/files chanchay-lambayeque/www/web/sites/default
        cp -rf pacifico/www/web/sites/default/files chillon-rimac-lurin/www/web/sites/default
        cp -rf pacifico/www/web/sites/default/files chira-piura/www/web/sites/default
        cp -rf pacifico/www/web/sites/default/files jequetepeque-zana/www/web/sites/default
        cp -rf pacifico/www/web/sites/default/files mantaro/www/web/sites/default
        cp -rf pacifico/www/web/sites/default/files mayo/www/web/sites/default
        cp -rf pacifico/www/web/sites/default/files pampas/www/web/sites/default
        cp -rf pacifico/www/web/sites/default/files quilca-chili/www/web/sites/default
        cp -rf pacifico/www/web/sites/default/files tumbes/www/web/sites/default
        cp -rf pacifico/www/web/sites/default/files urubamba/www/web/sites/default
          ;; 
     cu)
        docker exec -it srv-cuenca-mayo-apache drupal uc admin-crhc-mayo A-mayo-9003 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-mantaro-apache drupal uc admin-crhc-mantaro  A-mantaro-9004 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-pampas-apache drupal uc admin-crhc-pampas A-pampas-9005 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-urubamba-apache drupal uc admin-crhc-urubamba  A-urubamba-9006 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-pacifico-apache drupal uc admin-crh-pacifico A-pacifico-9002 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-tumbes-apache drupal uc admin-crhc-tumbes  A-tumbes-9007 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-chira-piura-apache drupal uc admin-crhc-chira-piura  A-chira-piura-9008 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-chanchay-lambayeque-apache drupal uc admin-crhc-chanchay-lambayeque  A-chanchay-lambayeque-9009 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-chancay-huaral-apache drupal uc admin-crhc-chancay-huaral  A-chancay-huaral-9010 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-caplina-locumba-apache drupal uc admin-crhc-caplina-locumba  A-caplina-locumba-9011 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-quilca-chili-apache drupal uc admin-crhc-quilca-chili  A-quilca-chili-9012 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-jequetepeque-zana-apache drupal uc admin-crhc-jequetepeque-zana  A-jequetepeque-zana-9013 --roles='admin'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-mayo-apache drupal uc editor-crhc-mayo E-mayo-9003 --roles='editor'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-mantaro-apache drupal uc editor-crhc-mantaro  E-mantaro-9004 --roles='editor'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-pampas-apache drupal uc editor-crhc-pampas E-pampas-9005 --roles='editor'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-urubamba-apache drupal uc editor-crhc-urubamba  E-urubamba-9006 --roles='editor'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-pacifico-apache drupal uc editor-crhc-pacifico E-pacifico-9002 --roles='editor'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-tumbes-apache drupal uc editor-crhc-tumbes  E-tumbes-9007 --roles='editor'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-chira-piura-apache drupal uc editor-crhc-chira-piura  E-chira-piura-9008 --roles='editor'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-chanchay-lambayeque-apache drupal uc editor-crhc-chanchay-lambayeque  E-chanchay-lambayeque-9009 --roles='editor'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-chancay-huaral-apache drupal uc editor-crhc-chancay-huaral  E-chancay-huaral-9010 --roles='editor'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-caplina-locumba-apache drupal uc editor-crhc-caplina-locumba  E-caplina-locumba-9011 --roles='editor'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-quilca-chili-apache drupal uc editor-crhc-quilca-chili  E-quilca-chili-9012 --roles='editor'   --email="test@ana.com"   --status="1"
        docker exec -it srv-cuenca-jequetepeque-zana-apache drupal uc editor-crhc-jequetepeque-zana  E-jequetepeque-zana-9013 --roles='editor'   --email="test@ana.com"   --status="1"
          ;;
     eu)
        docker exec -it srv-cuenca-pampas-apache drupal ud --user editor
        docker exec -it srv-cuenca-chanchay-lambayeque-apache drupal ud --user editor
        docker exec -it srv-cuenca-urubamba-apache drupal ud --user editor
        docker exec -it srv-cuenca-mayo-apache drupal ud --user editor
        docker exec -it srv-cuenca-jequetepeque-zana-apache drupal ud --user editor
        docker exec -it srv-cuenca-mantaro-apache drupal ud --user editor
        docker exec -it srv-cuenca-quilca-chili-apache drupal ud --user editor
        docker exec -it srv-cuenca-atlantico-apache drupal ud --user editor
        docker exec -it srv-cuenca-chancay-huaral-apache drupal ud --user editor
        docker exec -it srv-cuenca-pacifico-apache drupal ud --user editor
        docker exec -it srv-cuenca-caplina-locumba-apache drupal ud --user editor
        docker exec -it srv-cuenca-chira-piura-apache drupal ud --user editor
        docker exec -it srv-cuenca-tumbes-apache drupal ud --user editor
        docker exec -it srv-cuenca-chira-piura-apache drupal ud --user editor
        docker exec -it srv-cuenca-atlantico-apache drupal ud --user administrador
        docker exec -it srv-cuenca-mayo-apache drupal ud --user administrador
        docker exec -it srv-cuenca-mantaro-apache drupal ud --user administrador
        docker exec -it srv-cuenca-pampas-apache drupal ud --user administrador
        docker exec -it srv-cuenca-urubamba-apache drupal ud --user administrador
        docker exec -it srv-cuenca-pacifico-apache drupal ud --user administrador
        docker exec -it srv-cuenca-tumbes-apache drupal ud --user administrador
        docker exec -it srv-cuenca-chira-piura-apache drupal ud --user administrador
        docker exec -it srv-cuenca-chanchay-lambayeque-apache drupal ud --user administrador
        docker exec -it srv-cuenca-chancay-huaral-apache drupal ud --user administrador
        docker exec -it srv-cuenca-caplina-locumba-apache drupal ud --user administrador
        docker exec -it srv-cuenca-quilca-chili-apache drupal ud --user administrador
        docker exec -it srv-cuenca-jequetepeque-zana-apache drupal ud --user administrador
          ;;
esac